# Roteiro do vídeo (máx. 3:00) · Entrega 1 go-horse

Grave a tela com o app aberto (aluno à esquerda, painel `/cozinha` em outra aba). Fale ou use legenda. Alvo: **2:40**.

**0:00–0:20 · O problema**
Tela: título do app.
Fala: "A gente tem 15 minutos de intervalo: metade na fila, metade engolindo o lanche. Criamos a Cantina CESAR: você pede antes de descer, vê quanto tempo leva, paga e é avisado quando fica pronto."

**0:20–1:10 · App funcionando (aluno)**
Tela: escolha 2 coxinhas e 1 suco. Mostre a estimativa e o medidor mudando, a mensagem "Cabe nos seus 15 minutos". Digite o nome, escolha Pix e clique em "Fazer pedido".
Fala: "A estimativa soma o preparo dos pedidos à frente na fila mais o meu. Se passar de 15 minutos, o app avisa."

**1:10–1:40 · Cantina e aviso de pronto**
Tela: aba `/cozinha`: "Iniciar preparo" → "Marcar como pronto". Volte à aba do aluno e mostre o aviso verde "Seu pedido está pronto".
Fala: "A cantina toca a fila nesse painel e o aluno é avisado na hora, com som e vibração."

**1:40–2:30 · Princípios aplicados (mostre o código)**
- `models.py`: "**Ocultamento de informação**: `_status` e `_itens` são privados; o status só muda por `avancar()`, que não deixa pular etapa."
- `fila.py`: "**Responsabilidade Única**: a fila só cuida de ordem, posição e estimativa. Quem não é da fila nunca mexe na lista."
- Estrutura de pastas: "**Integridade conceitual**: pedido, item, fila, pagamento: o mesmo vocabulário da cantina em todo lugar."

**2:30–2:55 · Dívidas assumidas (go-horse honesto)**
Tela: `pagamento.py`.
Fala: "Aqui está o atalho: um if/elif para os meios de pagamento. Novo meio exige editar essa função, o que viola Aberto/Fechado. Na PoC final vamos trocar por uma interface com uma classe por meio de pagamento."

**2:55–3:00 · Fechamento**
Fala: "Cantina CESAR: menos fila, mais intervalo."
