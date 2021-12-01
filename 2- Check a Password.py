
def senhaok(SENHA):
    case1 = 0
    case2 = 0
    numero = 0
    if(len(SENHA) < 8): return False
    for i in range(0,len(SENHA)-1,1):
        if(SENHA[i].isupper()): case1 += 1  #isupper() retorna se todos os caracteres em uma string são maiúsculos ou não.
        elif(SENHA[i].islower()): case2 += 1 #islower() retorna se 1 ou + caracteres são minúsculos ou não.
        elif(SENHA[i].isnumeroeric()): numero += 1#isnumeroeric() retorna se 1 ou + caracteres são um numero.
    #se todos os parametros forem positivos é verdadeiro
    if(case1 >= 1 and case2 >= 1 and numero >= 1): return True
    else: return False

Senha = str(input('Digite a senha: '))

if(senhaok(Senha) == True):
    print('senha ok')
else:
    print('Digite outra senha')