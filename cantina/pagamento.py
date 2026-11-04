"""Pagamento do pedido.

GO-HORSE (dívida técnica assumida): cada forma de pagamento é um ramo de if/elif.
Para criar um novo meio de pagamento é preciso EDITAR esta função, o que viola o
princípio Aberto/Fechado. A PoC final vai resolver isso com uma interface e uma
classe por meio de pagamento.
"""

FORMAS = ("pix", "cartao", "dinheiro")


def pagar(pedido, forma):
    if forma == "pix":
        pedido.forma_pagamento = "pix"
        pedido.pago = True
        pedido.codigo_pagamento = f"PIX-{pedido.numero:04d}-CESAR"
    elif forma == "cartao":
        pedido.forma_pagamento = "cartao"
        pedido.pago = True
        pedido.codigo_pagamento = f"CARTAO-{pedido.numero:04d}-APROVADO"
    elif forma == "dinheiro":
        pedido.forma_pagamento = "dinheiro"
        pedido.pago = False  # paga no balcão, na retirada
        pedido.codigo_pagamento = None
    else:
        raise ValueError(f"Forma de pagamento desconhecida: {forma}")
