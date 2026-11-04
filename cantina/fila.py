"""A fila de pedidos: sabe a ordem, a posição e a estimativa de espera."""
from threading import Lock

from .models import Pedido, StatusPedido


class FilaDePedidos:
    def __init__(self):
        self._pedidos = []          # ninguém de fora mexe na lista diretamente
        self._proximo_numero = 1
        self._lock = Lock()

    def entrar(self, aluno, itens):
        with self._lock:
            pedido = Pedido(self._proximo_numero, aluno, itens)
            self._proximo_numero += 1
            self._pedidos.append(pedido)
            return pedido

    def buscar(self, numero):
        for pedido in self._pedidos:
            if pedido.numero == numero:
                return pedido
        return None

    def ativos(self):
        return [p for p in self._pedidos if p.ativo]

    def pedidos_do_painel(self):
        """Ativos + prontos aguardando retirada (o que a cozinha precisa ver)."""
        return [p for p in self._pedidos if p.status != StatusPedido.ENTREGUE]

    def posicao(self, pedido):
        """1 = é o próximo/está sendo preparado. 0 = não está mais na fila."""
        ativos = self.ativos()
        return ativos.index(pedido) + 1 if pedido in ativos else 0

    def minutos_na_fila(self):
        return sum(p.preparo_min for p in self.ativos())

    def estimativa_min(self, pedido):
        """Minutos até o pedido ficar pronto (preparo dos que estão à frente + o dele)."""
        total = 0
        for p in self.ativos():
            total += p.preparo_min
            if p is pedido:
                return total
        return 0
