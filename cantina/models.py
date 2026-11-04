"""Conceitos do domínio da cantina: item do cardápio e pedido."""
from dataclasses import dataclass


@dataclass(frozen=True)
class ItemCardapio:
    id: str
    nome: str
    preco: float
    preparo_min: int


class StatusPedido:
    AGUARDANDO = "aguardando"
    PREPARANDO = "preparando"
    PRONTO = "pronto"
    ENTREGUE = "entregue"

    # Ordem do ciclo de vida do pedido
    CICLO = [AGUARDANDO, PREPARANDO, PRONTO, ENTREGUE]


class Pedido:
    def __init__(self, numero, aluno, itens):
        self.numero = numero
        self.aluno = aluno
        self._itens = tuple(itens)          # princípio: ocultamento de informação
        self._status = StatusPedido.AGUARDANDO

        # GO-HORSE: campos públicos, quem mexe é o módulo de pagamento.
        self.forma_pagamento = None
        self.pago = False
        self.codigo_pagamento = None

    @property
    def itens(self):
        return self._itens

    @property
    def status(self):
        return self._status

    @property
    def total(self):
        return sum(item.preco for item in self._itens)

    @property
    def preparo_min(self):
        return sum(item.preparo_min for item in self._itens)

    @property
    def ativo(self):
        return self._status in (StatusPedido.AGUARDANDO, StatusPedido.PREPARANDO)

    def avancar(self):
        """Só permite andar para o próximo status do ciclo (sem pular etapas)."""
        i = StatusPedido.CICLO.index(self._status)
        if i == len(StatusPedido.CICLO) - 1:
            raise ValueError("Pedido já foi entregue.")
        self._status = StatusPedido.CICLO[i + 1]
