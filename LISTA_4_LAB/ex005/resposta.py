def resolver_autorama():
    try:
        K, N, M = map(int, input().split())
    except ValueError:
        print("Erro na linha de entrada inicial. Certifique-se de que são 3 números.")
        return
    estado_dos_carros = {}
    for i in range(1, N + 1):
        estado_dos_carros[i] = {
            'proximo_posto': 1,
            'postos_corretos': 0,
            'tempo_ultimo_posto': 0
        }
    for tempo_atual in range(1, M + 1):
        try:
            X, Y = map(int, input().split())
        except (ValueError, IndexError):
            continue
        ficha_carro_atual = estado_dos_carros[X]
        if Y == ficha_carro_atual['proximo_posto']:
            ficha_carro_atual['postos_corretos'] += 1
            ficha_carro_atual['tempo_ultimo_posto'] = tempo_atual
            ficha_carro_atual['proximo_posto'] = (Y % K) + 1
    lista_para_ordenar = []
    for id_carro, dados in estado_dos_carros.items():
        lista_para_ordenar.append({
            'id': id_carro,
            'pontos': dados['postos_corretos'],
            'tempo': dados['tempo_ultimo_posto']
        })
    classificacao = sorted(lista_para_ordenar, key=lambda x: (-x['pontos'], x['tempo']))
    resultado_final = [carro['id'] for carro in classificacao]
    print(*resultado_final)
if __name__ == "__main__":
    resolver_autorama()
