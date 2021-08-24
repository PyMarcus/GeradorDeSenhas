# gerando senhas aleatóriaas
import random, string


def geraSenha(tamanho):
    """===================================
    Gera uma senha com o tamanho fornecido
    ===================================="""
    senha = ''

    # inclui o tipo de caracteres que serão os formadores das senhas
    caracteres = string.ascii_letters + string.digits + '!@#$%¨&*()_'

    # selecionando os caracteres aleatóriamente
    rand = random.SystemRandom()  # gera de forma aleatória com base no SO
    for n in range(tamanho):
        senha = senha + rand.choice(caracteres)
    print(f"Senha gerada: {senha}")


if __name__ == '__main__':
    try:
        tamanho = int(input("Informe um tamanho para a senha (o recomendado é 16+): "))
    except ValueError:
        print("Argumento inválido")
    else:
        geraSenha(tamanho)