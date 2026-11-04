"""Cardápio do dia (dados fixos: é uma PoC, sem banco de dados)."""
from .models import ItemCardapio

CARDAPIO_DO_DIA = [
    ItemCardapio("coxinha", "Coxinha de frango", 6.50, 2),
    ItemCardapio("pastel", "Pastel de queijo", 8.00, 4),
    ItemCardapio("misto", "Misto quente", 8.50, 3),
    ItemCardapio("tapioca", "Tapioca de queijo coalho", 10.00, 4),
    ItemCardapio("cuscuz", "Cuscuz com ovo", 9.00, 3),
    ItemCardapio("bolo-rolo", "Fatia de bolo de rolo", 6.00, 1),
    ItemCardapio("suco", "Suco de caju", 7.00, 1),
    ItemCardapio("cafe", "Café", 4.00, 1),
]


def buscar_item(item_id):
    for item in CARDAPIO_DO_DIA:
        if item.id == item_id:
            return item
    return None
