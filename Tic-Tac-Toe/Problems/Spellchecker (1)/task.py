dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
text = str(input())
text = text.split()
errors = 0
for word in text:
    if word not in dictionary:
        print(word)
        errors = errors + 1
if errors == 0:
    print("OK")
