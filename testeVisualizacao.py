from parte3_visualizacao import VisualizadorResultado

labirinto_exemplo = [
    ['S', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '0'],
    ['1', '0', '0', 'E', '1']
]

caminho_simulado = [(0,0), (1,0), (1,1), (2,1), (3,1), (3,2), (3,3)]

visual = VisualizadorResultado(labirinto_exemplo)
visual.exibir_resultado_completo(caminho_simulado)