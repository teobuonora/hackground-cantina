# Cantina CESAR (versão go-horse)

App web para fazer os 15 minutos do intervalo renderem: o aluno **pede antes de descer**, vê a **estimativa de fila**, **paga** (Pix, cartão ou dinheiro) e é **avisado quando o pedido fica pronto**. A cantina tem um painel para tocar a fila.

> Hackathon Relâmpago #1 · FDS 2026.2 · CESAR School · Entrega 1 (go-horse)

## Decisões da stack
- **Python + Flask**: o time já domina Python e Flask sobe um servidor em poucas linhas.
- **Estado em memória, sem banco**: é uma PoC, o foco é o projeto das classes.
- **HTML + JS puro** (sem framework): menos dependências, nada para compilar.
- **IA (Claude)** escreveu a primeira versão do código; o time revisou e vai explicar as decisões.

## Integrantes e papéis
| Integrante | Papel |
|---|---|
| _[Nome 1]_ | Domínio e backend (`cantina/`) |
| _[Nome 2]_ | Interface do aluno (`templates/index.html`) |
| _[Nome 3]_ | Painel da cantina, testes e vídeo |

## Como rodar
```bash
git clone <url-deste-repositorio>
cd cantina-cesar
pip install -r requirements.txt
python app.py
```
- Aluno: http://localhost:5000
- Painel da cantina: http://localhost:5000/cozinha

## Onde estão os princípios do capítulo 5
| Princípio | Onde |
|---|---|
| **Integridade conceitual** | `cantina/models.py`, `fila.py`: o vocabulário é o da cantina (`Pedido`, `ItemCardapio`, `FilaDePedidos`) em todo o código |
| **Ocultamento de informação** | `Pedido._itens` e `_status` são privados e só mudam por `avancar()`; `FilaDePedidos._pedidos` nunca é exposta |
| **Responsabilidade Única** | `models.py` (o que é um pedido), `fila.py` (ordem e estimativa), `pagamento.py` (cobrança), `app.py` (HTTP) |
| **Imutabilidade/Coesão** | `ItemCardapio` é `frozen`; `Pedido.total` e `preparo_min` usam só os dados do próprio pedido |

## Dívidas conhecidas (vão virar a PoC final)
- `cantina/pagamento.py`: cadeia de `if/elif` para os meios de pagamento. **Viola Aberto/Fechado**; novo meio exige editar a função.
- `Pedido.pago` e `forma_pagamento` são públicos e alterados por fora. **Fere o ocultamento de informação.**
- `app.py` monta o dicionário do pedido conhecendo detalhes demais do domínio (**acoplamento**) e usa uma `fila` global.
