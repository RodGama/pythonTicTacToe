text = input()
words = text.split()
for word in words:
    # finish the code here
    if word.startswith("www.") or word.startswith("http://") or word.startswith("https://") or word.startswith("HTTP://") or word.startswith("HTTPS://") or word.startswith("WWW."):
        print(word)
