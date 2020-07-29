def palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    inverted_word = word[::-1]

    if word == inverted_word:
        return True
    else:
        return False

def run():
    word = input('Ingresa palabra: ')
    is_palindrome = palindrome(word)
    
    if is_palindrome == True:
        print('Tú palabra es palindromo.')
    else:
        print('Tú palabra no es palindromo.')


if __name__ == "__main__":
    print('¿TU PALABRA ES PALINDROMO?')
    run()