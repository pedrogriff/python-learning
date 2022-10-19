import pdb

x = [1, 2, 3]
y = 2
z = 3

print(z + y)

pdb.set_trace()
print(x + y)

try:
    x + y
    x = 1
    y = 1
except Exception as e:
    print("Erro: {}".format(e))
finally:
    print("Olá!")