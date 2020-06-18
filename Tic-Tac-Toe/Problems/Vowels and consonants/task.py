vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'z', 'y']
text = str(input())
for char in text:
    if not char.isalpha():
        break
    if char.lower() in vogais:
        print("vowel")
    else:
        print("consonant")


