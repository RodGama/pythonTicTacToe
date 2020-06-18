a = str(input())
nums = []
while a != ".":
    nums.append(float(a))
    a = str(input())
print(min(nums))
