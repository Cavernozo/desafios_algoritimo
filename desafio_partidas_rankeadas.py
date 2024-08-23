def calculo(vitoria, derrotas):
    saldo = vitoria - derrotas
    return saldo

def nivel_ranked(saldovitorias):
    if saldovitorias <= 10:
        ranke = "Ferro"
        return ranke
    elif saldovitorias >= 11 and saldovitorias <= 20:
        ranke = "Bronze"
        return ranke
    elif saldovitorias >= 21 and saldovitorias <= 50:
        ranke = "Prata"
        return ranke
    elif saldovitorias >= 51 and saldovitorias <= 80:
        ranke = "Ouro"
        return ranke
    elif saldovitorias >= 81 and saldovitorias <= 90:
        ranke = "Diamante"
        return ranke
    elif saldovitorias >= 91 and saldovitorias <= 100:
        ranke = "Lendario"
        return ranke
    else:
        ranke = "Imortal"
        return ranke
    
while True:
    vitorias = int(input("Numero de vitorias: "))
    derrotas = int(input("Numero de derrotas: "))
    saldo = calculo(vitorias, derrotas)
    print(nivel_ranked(saldo))
    opcao = (input("Quer continuar: [digite N para parar]")).upper()
    if opcao == "N":
        break