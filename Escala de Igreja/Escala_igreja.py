import random
import shutil

def limpa_tela():
    print("\n" * shutil.get_terminal_size().lines)

while True:
    print("+---------------------------------------+")
    print("|     \033[0;30mGERADOR DE ESCALAS DE MISSAS\033[0;0m      |")
    print("+---------------------------------------+")

    dataMissa = input("Informe a data da missa: ")
    qtdeMissas = int(input("Quantas missas serão realizadas? : "))
    qtdeCoroinhas = int(input("Quantos Coroinhas são necessários em cada missa? : "))

    arranjo = (qtdeCoroinhas * qtdeMissas)

    print(f"\nPara o dia \033[1;93m{dataMissa}\033[0;0m, serão relizados \033[1;93m{qtdeMissas}\033[0;0m missas e serão necessários um total de \033[1;93m%.0f\033[0;0m coroinhas para as celebrações!\n" %arranjo)

    print(f"\n|--------Escala das \033[1;93m{qtdeMissas}\033[0;0m missas--------|\n")

    listarCoroinhas = []
    for i in range(arranjo):
        lista = input(f"Digite o nome do coroinha \033[1;30;107m{i+1}\033[0;0;0m de \033[1;30;107m{arranjo}\033[0;0;0m escalado: ")
        listarCoroinhas.append(lista)
    random.shuffle(listarCoroinhas)
    print("\n|--------------------------------------------------|\n")

    listarHorarios = []
    for i in range(qtdeMissas):
        horario = input(f"Digite o horário da missa \033[1;93;107m{i+1}\033[0;0;0m de \033[1;93;107m{qtdeMissas}\033[0;0;0m: ")
        listarHorarios.append(horario)
    print("\n|--------------------------------------------------|\n")


    for i in range(qtdeMissas):
        print(f"\033[0;33mEscala da missa dia \033[0;30m{dataMissa} \033[0;33màs: \033[1;93;44m"+listarHorarios[i]+"\033[0;0;0m")
        lista = listarCoroinhas

        for c in range(qtdeCoroinhas):
            print(f"  - Coroinha: \033[1;93m{lista[c]}\033[0;0m\n")

        del (lista[:qtdeCoroinhas])

    continua = input("\n\nContinuar a gerar escalas? (S/N): ")
    if continua == "S" or continua =="s":
        limpa_tela()
    else:
        limpa_tela()
        exit()