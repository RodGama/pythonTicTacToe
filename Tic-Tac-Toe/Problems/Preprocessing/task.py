text = str(input())
text = text.replace("!", "")
text = text.replace(".", " ")
text = text.replace(" ' ", "")
text = text.replace("?", " ")
text = text.replace(",", " ")
text = text.lower()
print(text)