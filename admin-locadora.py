import os

carros = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130)
]
alugados = []

print("===========")
print("Bem vindo à locadora de carros!")
print("===========")
print("O que deseja fazer?")
print("0 - Mostrar portfolio | 1 - Alugar um carro | 2 - Devolver um carro")
opt = int(input())

portfolio = {
    "[0]": "Chevrolet Tracker - R$ 120/dia",
    "[1]": "Chevrolet Onix - R$ 90/dia",
    "[2]": "Chevrolet Spin - R$ 150/dia",
    "[3]": "Hyundai HB20 - R$ 85/dia",
    "[4]": "Hyundai Tucson - R$ 120/dia",
    "[5]": "Fiat Uno - R$ 60/dia",
    "[6]": "Fiat Mobi - R$ 70/dia",
    "[7]": "Fiat Pulse - R$ 130/dia"
}

while True:
    os.system("clear")
    i = 0
    for op, name in portfolio.items():
        print(i, ":", name)
        i += 1
    print("")
    print("O que deseja fazer?")
    print("0 - Mostrar portfolio | 1 - Alugar um carro | 2 - Devolver um carro")
    op = int(input())
    op_string = list(portfolio.keys())[op]

