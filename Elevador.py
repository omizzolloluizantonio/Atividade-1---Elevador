#Desenvolva um sistema capaz de coletar, processar e apresentar informações obtidas a partir de uma pesquisa. A pesquisa tem como objetivo entender o perfil dos moradores de um prédio, para isso, será necessário coletar respostas para as seguintes perguntas: Qual elevador que utilizava com mais frequência; (Elevador A, Elevador B, Elevador C) Qual período em que utilizava o elevador: (M=Matutino, V=Vespertino, N=Noturno) Construa um algoritmo que faça a leitura, calcule e mostre: Qual o elevador mais utilizado; Qual o período mais utilizado de todos; Qual a diferença porcentual entre o mais usado dos horários e o menos usado; Qual a porcentagem de uso de cada elevador; Qual a porcentagem de uso de cada período. O programa deve ser capaz de receber as respostas de 100 moradores do prédio.
# Inicializando contadores para cada elevador e período
elevador_A = 0
elevador_B = 0
elevador_C = 0
periodo_M = 0
periodo_V = 0
periodo_N = 0

def coletar_respostas():
    global elevador_A, elevador_B, elevador_C, periodo_M, periodo_V, periodo_N
    
    for i in range(100):
        print(f"Morador {i + 1}:")
        
        # Coletando a resposta do elevador
        while True:
            elevador = input("Qual elevador você utiliza com mais frequência? (A/B/C): ").strip().upper()
            if elevador in ['A', 'B', 'C']:
                if elevador == 'A':
                    elevador_A += 1
                elif elevador == 'B':
                    elevador_B += 1
                elif elevador == 'C':
                    elevador_C += 1
                break
            else:
                print("Resposta inválida. Por favor, escolha A, B ou C.")
        
        # Coletando a resposta do período
        while True:
            periodo = input("Qual período você utiliza o elevador? (M=Matutino, V=Vespertino, N=Noturno): ").strip().upper()
            if periodo in ['M', 'V', 'N']:
                if periodo == 'M':
                    periodo_M += 1
                elif periodo == 'V':
                    periodo_V += 1
                elif periodo == 'N':
                    periodo_N += 1
                break
            else:
                print("Resposta inválida. Por favor, escolha M, V ou N.")

def calcular_resultados():
    total_elevadores = elevador_A + elevador_B + elevador_C
    total_periodos = periodo_M + periodo_V + periodo_N
    
    # Determinando o elevador mais utilizado
    if elevador_A > elevador_B and elevador_A > elevador_C:
        elevador_mais_utilizado = 'A'
    elif elevador_B > elevador_A and elevador_B > elevador_C:
        elevador_mais_utilizado = 'B'
    else:
        elevador_mais_utilizado = 'C'
    
    # Determinando o período mais utilizado
    if periodo_M > periodo_V and periodo_M > periodo_N:
        periodo_mais_utilizado = 'M'
    elif periodo_V > periodo_M and periodo_V > periodo_N:
        periodo_mais_utilizado = 'V'
    else:
        periodo_mais_utilizado = 'N'
    
    # Calculando a diferença porcentual entre o mais usado e o menos usado dos horários
    porcentagem_diferenca = 0
    if total_periodos > 0:
        max_periodo = max(periodo_M, periodo_V, periodo_N)
        min_periodo = min(periodo_M, periodo_V, periodo_N)
        porcentagem_diferenca = ((max_periodo - min_periodo) / total_periodos) * 100
    
    # Calculando a porcentagem de uso de cada elevador
    porcentagem_elevador_A = (elevador_A / total_elevadores) * 100 if total_elevadores > 0 else 0
    porcentagem_elevador_B = (elevador_B / total_elevadores) * 100 if total_elevadores > 0 else 0
    porcentagem_elevador_C = (elevador_C / total_elevadores) * 100 if total_elevadores > 0 else 0
    
    # Calculando a porcentagem de uso de cada período
    porcentagem_periodo_M = (periodo_M / total_periodos) * 100 if total_periodos > 0 else 0
    porcentagem_periodo_V = (periodo_V / total_periodos) * 100 if total_periodos > 0 else 0
    porcentagem_periodo_N = (periodo_N / total_periodos) * 100 if total_periodos > 0 else 0

    # Exibindo os resultados
    print("\nResultados da Pesquisa:")
    print(f"Elevador mais utilizado: {elevador_mais_utilizado}")
    print(f"Período mais utilizado: {periodo_mais_utilizado}")
    print(f"Diferença porcentual entre o mais usado e o menos usado dos horários: {porcentagem_diferenca:.2f}%")
    print(f"Porcentagem de uso do Elevador A: {porcentagem_elevador_A:.2f}%")
    print(f"Porcentagem de uso do Elevador B: {porcentagem_elevador_B:.2f}%")
    print(f"Porcentagem de uso do Elevador C: {porcentagem_elevador_C:.2f}%")
    print(f"Porcentagem de uso do Período Matutino: {porcentagem_periodo_M:.2f}%")
    print(f"Porcentagem de uso do Período Vespertino: {porcentagem_periodo_V:.2f}%")
    print(f"Porcentagem de uso do Período Noturno: {porcentagem_periodo_N:.2f}%")
