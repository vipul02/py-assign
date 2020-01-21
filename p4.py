def D3M1(args): 
    return[[ [0 for col in range(args[0])] for col in range(args[1])] for row in range(args[2])] 

# Another method to do this
def D3M2(args): 
    return [[[0]*args[0]]*args[1]]*args[1]

args = list(map(int, input('Enter three nums (Eg. 3 5 8): ').split(' ')))

print(D3M1(args), end='\n\n--------------------------------------\n\n')
print(D3M2(args))