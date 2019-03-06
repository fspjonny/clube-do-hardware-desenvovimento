import random
import shutil

def limpa_tela():
    print("\n" * shutil.get_terminal_size().lines)

while True:
    print("+---------------------------------------+")
    print("|    GERADOR DE ESCALAS DE MISSAS       |")
    print("+---------------------------------------+")

    qtdeMissas = int(input("Quantas missas serão realizadas no mês? : "))

    diaHoraMissa = []
    for i in range(qtdeMissas):
        dataHoraMissa = input("Informe a Data e a Hora da {}º missa: ".format(i+1))
        diaHoraMissa.append(dataHoraMissa)

    listaCoroinhas = ["Rebeca","Levi","Yasmin","Ivan","Luana","Eric","Leticia","Ilana","Elym","Kauan"]
    random.shuffle(listaCoroinhas)

    for i in range(qtdeMissas):
        lista = listaCoroinhas
        random.shuffle(lista)

        print(f"\nEscala da missa dia {diaHoraMissa[i]}")
        for c in range(1):
            resultado = ", ".join(random.sample(lista,3))
            print (f"  Coroinhas : {resultado}")

    continua = input("\n\nContinuar a gerar escalas? (S/N): ")
    if continua == "S" or continua =="s":
        limpa_tela()
    else:
        limpa_tela()
        exit()