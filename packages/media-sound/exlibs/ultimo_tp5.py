titulo = input()
auto = input()
dni = int(input())
area = int(input())
max1 = 0
codigo_area = {1: "", 2: "", 3:""}
digitos = ['','','','','','','','','']
while (dni != 0) && (area != -1):
	dni2 = dni
	while (dni2 != 0):
		resto = dni2 / 10
		digitos [resto] += 1
		dni2 = dni2 / 10
	print (digitos)

	codigo_area [area] += 1

	titulo = input()
	auto = input()
	dni = int(input())
	area = int(input())

for i in codigo_area :
	if (i > max1):
		max1 = i

print (max1)
