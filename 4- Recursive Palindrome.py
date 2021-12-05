word = input("Input: ")
if str(word) == "".join(reversed(word)) :
    print("Palindromo")
else:
    print("Não é um Palindromo")