money = float(input())
Chicken = 23
Goat = 678
Pig = 1296
Cow = 3848
Sheep = 6769
basket = [[0, " sheep "], [0, " cow"], [0, " pig"], [0, " goat"], [0, " chicken"]]
while money >= Sheep:
    if money >= Sheep:
        money = money - Sheep
        basket[0][0] = basket[0][0] + 1
while money >= Cow:
    if money >= Cow:
        money = money - Cow
        basket[1][0] = basket[1][0] + 1
while money >= Pig:
    if money >= Pig:
        money = money - Pig
        basket[2][0] = basket[2][0] + 1
while money >= Goat:
    if money >= Goat:
        money = money - Goat
        basket[3][0] = basket[3][0] + 1
while money >= Chicken:
    if money >= Chicken:
        money = money - Chicken
        basket[4][0] = basket[4][0] + 1

if basket[1][0] > 1:
    basket[1][1] = basket[1][1] + "s "
elif basket[2][0] > 1:
    basket[2][1] = basket[2][1] + "s "
elif basket[3][0] > 1:
    basket[3][1] = basket[3][1] + "s "
elif basket[4][0] > 1:
    basket[4][1] = basket[4][1] + "s "

if basket[0][0] > 0:
    print(str(basket[0][0]) + basket[0][1])
elif basket[1][0] > 0:
    print(str(basket[1][0]) + basket[1][1])
elif basket[2][0] > 0:
    print(str(basket[2][0]) + basket[2][1])
elif basket[3][0] > 0:
    print(str(basket[3][0]) + basket[3][1])
elif basket[4][0] > 0:
    print(str(basket[4][0]) + basket[4][1])
else:
    print("None")
