def cadastrar_aluno():
    alunos = {}

    while True:
        nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ").strip()
        if nome.lower() == 'fim':
            break
        if nome == "":
            print("Nome não pode ser vazio.")
            continue

        notas = []
        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Digite a {i}ª nota de {nome} (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
        
        alunos[nome] = notas
        print(f"Aluno {nome} cadastrado com sucesso!\n")

    return alunos

def calcular_medias(alunos):
    medias = {}
    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        medias[nome] = media
    return medias

def exibir_resultados(medias):
    print("\n=== Médias dos alunos ===")
    for nome, media in medias.items():
        print(f"{nome}: {media:.2f}")

    melhor_aluno = max(medias, key=medias.get)
    print(f"\nAluno com a maior média: {melhor_aluno} ({medias[melhor_aluno]:.2f})")

alunos = cadastrar_aluno()
medias = calcular_medias(alunos)
exibir_resultados(medias)
