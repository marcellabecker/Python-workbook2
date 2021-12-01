#codifica adicionando 3 letras ao cada um do imput
def codificar(txt):
    txt2 = ''
    minusculo = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
    maiusculo = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']
    for i in range(0, len(txt), 1):
        for j in range(0, len(minusculo)-3,1):
            if(txt[i] == minusculo[j]):
                txt2 += minusculo[j+3]
            elif(txt[i] == maiusculo[j]):
                txt2 += maiusculo[j+3]
    return txt2
#descodifica diminuindo 3 letras do imput
def descodificar(txt):
    txt2 = ''
    minusculo = ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    maiusculo = ['X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(0, len(txt), 1):
        for j in range(0, len(minusculo)-3,1):
            if(txt[i] == minusculo[j]):
                txt2 += minusculo[j-3]
            elif(txt[i] == maiusculo[j]):
                txt2 += maiusculo[j-3]
    return txt2
# 1 codificar vai para função 1 e 0 descodificar vai para função 2
x = int(input('Se você deseja encriptar a mensagem digite 1, se deseja descriptar digite 0: '))
#imput do texto
t = str(input('Digite o texto: '))
if(x == 1):
    print(codificar(t))
elif(x == 0):
    print(descodificar(t))
else:
    print('Digite 1 ou 0')