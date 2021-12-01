#mostra se um numero é perfeito ou não
def perfect_num(num):
    cont = 0
    for i in range(1, num, 1): 
        if(num % i == 0):
            cont += i
    if(cont == num):
        return True
    else:
        return False
#printa numeros perfeitos de 1 a 10.000
print('Numeros Perfeitos')
for i in range(1, 10000, 1):
    if(perfect_num(i)):
        print(i)