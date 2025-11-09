# Labirinto 2D com Algoritmo A*

**Disciplina:** Fundamentos de Projeto e Análise de Algoritmos (FPAA)  
**Professor:** João Paulo Carneiro Aramuni

**Integrantes**
- Pedro de Sousa Motta
- Hitalo Silveira Porto
- Leonardo Vieira Machado
- Tiago Assunção de Sousa

---

## Descrição do Projeto

Este trabalho apresenta um resolvedor automático de labirintos modelados como matrizes bidimensionais. Cada célula da matriz pode assumir os valores `0` (caminho livre), `1` (obstáculo), `S` (ponto inicial) e `E` (ponto final). O objetivo é conduzir um agente desde `S` até `E` evitando obstáculos e encontrando um trajeto com o menor custo possível.

Para isso utilizamos o algoritmo de busca informada **A\***, que combina custo acumulado e heurística para guiar a exploração do labirinto de maneira eficiente, priorizando caminhos promissores até alcançar o objetivo ou concluir que não existe solução viável.

## Regras do Labirinto
- O movimento é ortogonal: cima, baixo, esquerda e direita (4 direções).
- Cada passo possui custo unitário (1).
- O labirinto deve conter exatamente um `S` e um `E`; caso contrário, o programa acusa erro de validação.
- Quando não há caminho possível entre `S` e `E`, o programa informa que não existe solução e exibe o labirinto original.

## Como Executar o Projeto

### Pré-requisitos
- Python 3.10 ou superior.
- Não há dependências externas além da biblioteca padrão.

### Como rodar
No terminal, dentro da pasta do projeto:
```bash
python parte4_integração.py
```

### Formato da entrada
- O usuário seleciona um dos labirintos de exemplo ou digita um novo labirinto diretamente no console.
- Cada linha deve ser composta por valores separados por espaço. Digite `fim` para encerrar a entrada personalizada.

Exemplo de entrada manual:
```
S 0 1 0 0
0 0 1 0 1
1 0 1 0 0
1 0 0 E 1
fim
```

### Saída
- Labirinto original com o caminho encontrado destacado com `*`.
- Lista de coordenadas na ordem percorrida.
- Mensagens de erro ou aviso em caso de labirintos inválidos ou sem solução.

## Algoritmo Utilizado – A*

### Ideia geral
O algoritmo A\* mantém uma estrutura de nós abertos (candidatos a expansão) e um conjunto de nós fechados (já explorados). Cada posição do labirinto é tratada como um nó. A cada iteração, o nó com menor valor de `f(n) = g(n) + h(n)` é escolhido para expansão:
- `g(n)`: custo real acumulado desde `S` até o nó atual (número de passos).
- `h(n)`: estimativa heurística do custo até `E`.

Se o nó extraído é `E`, reconstruímos o caminho percorrendo os "pais" de cada nó até chegar a `S`. Caso a lista de abertos se esgote sem alcançar `E`, concluímos que não há solução.

### Heurística de Manhattan
A heurística adotada é a **distância de Manhattan**:
```
h(n) = |linha_atual - linha_E| + |coluna_atual - coluna_E|
```
Ela mede quantos passos ortogonais seriam necessários para alcançar `E` ignorando obstáculos, guiando a busca na direção correta sem superestimar o custo.

### Implementação no código
- A classe `PathFinder` em `parte2_percurso.py` encapsula o algoritmo.  
- Cada nó é representado por um par `(linha, coluna)`, enquanto o dicionário `came_from` guarda o pai de cada nó para reconstrução do caminho.  
- A fila de prioridade `open_set` armazena tuplas `(f_score, g_score, nó, pai)`, sempre priorizando o menor `f`.  
- A função `executar_a_estrela()`:
  1. Localiza `S` e `E`.
  2. Insere o nó inicial em `open_set`.
  3. Enquanto houver nós abertos:
     - Remove o nó com menor `f`.
     - Se este nó for `E`, reconstrói e retorna o caminho.
     - Caso contrário, gera vizinhos válidos (dentro do labirinto e diferentes de `1`), calcula novos custos e atualiza a fila.
  4. Retorna lista vazia se não houver caminho ou mensagem de erro se a entrada for inválida.

## Exemplos de Entrada e Saída

### Exemplo 1 – Labirinto com solução
Entrada:
```
S 0 1 0 0
0 0 1 0 1
1 0 1 0 0
1 0 0 E 1
```

Saída (resumo):
```
Labirinto com caminho encontrado:

S * 1 0 0
* * 1 0 1
1 * 1 0 0
1 * * E 1

Caminho (lista de coordenadas):
(0,0) → (1,0) → (1,1) → (2,1) → (3,1) → (3,2) → (3,3)

Caminho exibido com sucesso!
```

### Exemplo 2 – Labirinto sem solução
Entrada:
```
S 1 1
1 1 0
0 0 E
```

Saída (resumo):
```
Nenhum caminho possível entre S e E.

S 1 1
1 1 0
0 0 E
```

## Estrutura do Projeto
- `parte1_menu.py`: menu interativo, carregamento e validação dos labirintos.
- `parte2_percurso.py`: implementação do algoritmo A\*.
- `parte3_visualizacao.py`: marcação do caminho e exibição formatada do resultado.
- `parte4_integração.py`: ponto de entrada que integra todas as partes.
- `testeVisualizacao.py`: script auxiliar para testar a visualização independentemente.

## Como testar com outros labirintos
Execute `parte4_integração.py` e escolha a opção de criar um labirinto personalizado. Digite a nova matriz seguindo o formato especificado. Também é possível editar diretamente os exemplos dentro de `parte1_menu.py` para registrar novos casos de teste (com ou sem solução).

