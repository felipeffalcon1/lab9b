ex 1)

a) Cobertura de ramos: 100%. Foram gerados 36 mutantes no total. Mortos: 24. Vivos: 12. Escore inicial MS = 24/36 = 66,67%.

b) Os mutantes vivos ficaram em linhas de trechos de código que a suíte inicial com 2 testes não cobriu direito ou que tinham checagens parciais:
- Mutantes 3 e 4: alterações no primeiro `if` (validação de peso <= 0 ou peso > 30).
- Mutantes 7: alteração na exceção do peso.
- Mutantes 11, 12 e 13: alterações no `if` de distancia (< 0 ou > 5000) e na exceção de distancia invalida.
- Mutantes 16, 19, 20: alterações na condição de peso > 20 (Transportadora) e limite de distancia <= 10 (Motoboy).
- Mutantes 25, 29, 30: alterações nos retornos dos fretes expresso e economico.

c) Foram adicionados testes cobrindo Transportadora (peso 25, distancia 100), Motoboy (peso 5, distancia 10) e os limites das exceções de peso e distancia invalida. Com isso todos os mutantes não equivalentes foram mortos e o MS final subiu para 100%.

d) Usando `str(erro.value) == msg` o teste apenas compara a string sem validar direito a classe da exceção lançada, o que pode deixar mutantes vivos se a exceção mudar. Já com `pytest.raises(ValueError, match=msg)` o pytest valida tanto o tipo exato da exceção quanto a mensagem exata por regex. Isso força o mutante que altera a classe ou tipo de erro a falhar, aumentando a precisão e matando mutantes relacionados à criação e lançamento da exceção.

---

ex 2)

a) A cobertura de ramos deu 100% porque a suíte inicial passou por todas as linhas do código e seguiu o caminho do `if`. Porém o MS ficou baixo (~23%) porque o unico teste usava `assert cashback(...) > 0`. Ele garantia que entrava no `if`, mas não checava se o valor retornado estava correto.

b) Ao trocar o `> 0` por `assert cashback([50, 100, 200]) == 15.0`, a maioria dos mutantes morre na hora. Ainda continuam vivos 3 mutantes (relacionados a lista vazia ou valores exatamente na borda de 100).

c) Para a condição RIPP (Alcançar, Infectar, Propagar, Revelar):
- Mutante 10: Alcance e infecção ocorrem, mas não propaga/revela porque falta testar lista vazia `[]`.
- Mutantes 12 e 13: Alteram a condição `>= 100` para `> 100`. Alcança e infecta quando o valor é 100, mas como não tinha entrada com valor exato de 100.0 isolado para checar o contorno, o erro não se revela no assert.

d) Foram adicionados os casos de teste com lista vazia `[]`, valor abaixo do limite `[99.99]` e valor exatamente no limite `[100.0]`. A nova entrada precisou ter valores exatamente na fronteira do `if` (100.0 e 99.99) para matar os mutantes de operadores relacionais e garantir MS = 100%.

---

ex 3)

a) Rodei o mutmut e 6 mutantes ficaram vivos na suíte inicial (3 no menor_preco e 3 no dia_da_compra).

b) Classificação dos vivos:
- Em `menor_preco`: trocar `<` por `<=` no laço gera mutante EQUIVALENTE. Se dois preços forem iguais e menores que os anteriores, atualizar o valor da variável com o mesmo número não altera o valor final retornado pela função.
- Em `dia_da_compra`: trocar `<=` por `<` NÃO É EQUIVALENTE. A especificação pede a posição do ÚLTIMO dia com menor preço. Se trocar por `<`, a função devolve o PRIMEIRO dia em caso de empate.
- Os outros vivos eram checagens de validação da lista vazia e bordas de laço não cobertas.

c) Adicionei o teste de desempate `assert dia_da_compra([10, 20, 10]) == 2` para pegar o ultimo dia e testes com `pytest.raises` para a lista vazia. O MS antes estava em 72,7% e depois das correções (descontando o equivalente do menor_preco) o MS final foi a 100%.

d) Em `menor_preco`, a função retorna o menor valor da lista. Se houver empate (ex: [10, 10]), atualizar a variável do menor valor na primeira vez ou na segunda dá exatamente 10, então a troca de `<` por `<=` não altera o resultado final (equivalente). Em `dia_da_compra`, o que importa é o índice (posição) do dia. Se houver empate, trocar `<=` por `<` faz a função parar no primeiro índice em vez de atualizar para o último, mudando a resposta e quebrando a especificação (não equivalente).

---

ex 4)

a) Por valor-limite nas partições (dias < 0, 0 a 5, 6 a 60, > 60):
- Limites validos de dias: 0, 5, 6, 60.
- Limites invalidos (exceção): -1, 61.

b) Essa suíte por valor-limite já atingiu 100% de cobertura de ramos e matou 21 dos 26 mutantes (MS inicial alto de ~80,7%).

c) Os mutantes que sobraram vivos eram ajustes finos no cálculo de arredondamento e contornos das exceções. Adicionando os testes exatos nos limites das bordas -1, 0, 5, 6, 60 e 61 todos os mutantes não equivalentes morrem, chegando a 100% de MS final.

d e e) Mutante de segunda ordem: se aplicarmos duas alterações juntas no código (ex: trocar `dias <= 5` por `dias < 5` E trocar `(dias - 5)` por `(dias - 4)`), a suíte mata esse mutante composto. Isso confirma o Efeito de Acoplamento de Offutt (1992): testes projetados para detectar e matar mutantes simples (de primeira ordem) são eficientes e acabam matando também a grande maioria dos mutantes complexos / de ordem superior.
