# Number div by 7 and 5 is number divisible by 35
def div(n):
    for num in range(n):
        if num % 35 == 0:
            yield num
    
n = int(input())
for _ in div(n):
    print(_, end = ",")