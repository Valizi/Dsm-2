frutas = ["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

# imprimindo apenas a fruta na terceira posição
print(f"Fruta na terceira posição: {frutas[2]}")

# substituindo pera por melancia
frutas[3] = "melancia"

# imprimindo a lista
print(frutas)

print(25 * '-')

# percorrendo a lista e exibindo seus elementos do primeiro ao último
for f in frutas:
    print(f)
print(30 * '-')

# percorrendo a lista e exibindo seus elementos do último para o primeiro
for f in reversed(frutas):
    print(f)
print(30 * '-')

# exibindo a posição e o valor de cada elemento da lista
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")

print(25 * '-')

for i in range(len(frutas)-1, -1, -1):
    print(f"{i}: {frutas[i]}")

print(25 * '-')


