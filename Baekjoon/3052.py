nums = []

for i in range(10) :
    n = int(input())
    nums.append(n % 42)

print(len(set(nums)))
