palavra = input('Palavra: ')
palindrome = palavra == palavra[::-1]
print (f'{palavra} e palindrome?')
print (palindrome)