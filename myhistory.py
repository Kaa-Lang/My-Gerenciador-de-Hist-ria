import random

# Função que gera a introdução da história
def gerar_introducao():
    introducoes = ["Era uma vez",  "Em um belo dia", "Nas profundezas de uma floresta encantada"]
    return random.choice(introducoes)

# Função que gera o desenvolvimento da história
def gerar_desenvolvimento():
    desenvolvimentos = ["uma linda princesa", "uma fada", "um mundo mágico com muitas princesas, principes, fadas, um rei e uma rainha"]
    return random.choice(desenvolvimentos)

# Função que gera o final da história
def gerar_final():
    finais = ["finalizando os seus cachos.", "que ficava muito feliz a voar.", "muitos rigorosos."]
    return random.choice(finais)

# Função principal que gera toda a história
def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia

# Exibe a história gerada
if __name__ == "__main__":
    print(gerar_historia())