heroi = input("nome: ")
xp = int(input("xp: "))
nivel = ''

if xp <= 1000:
    nivel = "Ferro"

elif xp >= 1001 and xp <= 2000:
    nivel = "Bronze"

elif xp >= 2001 and xp <= 5000:
    nivel = "Prata"

elif xp >= 6001 and xp <= 7000:
    nivel = "Ouro"

elif xp >= 7001 and xp <= 8000:
    nivel = "Platina"

elif xp >= 8001 and xp <= 9000:
    nivel = "Ascendente"

elif xp >= 9001 and xp <= 10000:
    nivel = "Imortal"

else:
    nivel = "Radiante"

print(f"O heroi com o nome: {heroi} está no nivel: {nivel}")
