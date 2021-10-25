from typing import Text


def palindrome(text):
    return text == text[::-1]

def main():
    text = input("Input: ")
    if(palindrome(test)): 
     print(text + " é um palindromo")
    else:
     print(text + " não é palindromo")
        
if __name__ == "__main__": main()