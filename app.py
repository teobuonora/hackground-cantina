"""Cantina CESAR: pedido antecipado com estimativa de fila e aviso de 'pedido pronto'."""
from flask import Flask, jsonify, render_template, request

from cantina.cardapio import CARDAPIO_DO_DIA, buscar_item
from cantina.fila import FilaDePedidos
from cantina.pagamento import FORMAS, pagar

INTERVALO_MIN = 15

app = Flask(__name__)
fila = FilaDePedidos()  # GO-HORSE: estado global em memória (sem banco, sem deploy)


def pedido_para_dict(pedido):
    """GO-HORSE: a rota conhece detalhes demais do Pedido (acoplamento)."""
    return {
        "numero": pedido.numero,
        "aluno": pedido.aluno,
        "status": pedido.status,
        "itens": [i.nome for i in pedido.itens],
        "total": pedido.total,
        "pago": pedido.pago,
        "forma_pagamento": pedido.forma_pagamento,
        "codigo_pagamento": pedido.codigo_pagamento,
        "posicao": fila.posicao(pedido),
        "estimativa_min": fila.estimativa_min(pedido),
        "cabe_no_intervalo": fila.estimativa_min(pedido) <= INTERVALO_MIN,
    }


@app.get("/")
def pagina_aluno():
    return render_template("index.html", intervalo=INTERVALO_MIN)


@app.get("/cozinha")
def pagina_cozinha():
    return render_template("cozinha.html")


@app.get("/api/cardapio")
def api_cardapio():
    return jsonify([vars(i) for i in CARDAPIO_DO_DIA])


@app.get("/api/fila")
def api_fila():
    return jsonify({"minutos_na_fila": fila.minutos_na_fila(), "pedidos_ativos": len(fila.ativos())})


@app.post("/api/pedidos")
def api_criar_pedido():
    dados = request.get_json(silent=True) or {}
    aluno = (dados.get("aluno") or "").strip()
    if not aluno:
        return jsonify({"erro": "Informe seu nome."}), 400

    itens = []
    for linha in dados.get("itens", []):
        item = buscar_item(linha.get("id"))
        qtd = int(linha.get("qtd", 0))
        if item is None or qtd < 1 or qtd > 10:
            return jsonify({"erro": "Item ou quantidade inválida."}), 400
        itens.extend([item] * qtd)
    if not itens:
        return jsonify({"erro": "Escolha pelo menos um item."}), 400

    forma = dados.get("pagamento", "")
    if forma not in FORMAS:
        return jsonify({"erro": "Escolha uma forma de pagamento."}), 400

    pedido = fila.entrar(aluno, itens)
    pagar(pedido, forma)
    return jsonify(pedido_para_dict(pedido)), 201


@app.get("/api/pedidos/<int:numero>")
def api_ver_pedido(numero):
    pedido = fila.buscar(numero)
    if pedido is None:
        return jsonify({"erro": "Pedido não encontrado."}), 404
    return jsonify(pedido_para_dict(pedido))


@app.get("/api/painel")
def api_painel():
    return jsonify([pedido_para_dict(p) for p in fila.pedidos_do_painel()])


@app.post("/api/pedidos/<int:numero>/avancar")
def api_avancar(numero):
    pedido = fila.buscar(numero)
    if pedido is None:
        return jsonify({"erro": "Pedido não encontrado."}), 404
    try:
        pedido.avancar()
    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400
    return jsonify(pedido_para_dict(pedido))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
