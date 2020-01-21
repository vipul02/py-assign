class ReverseIter:
    
    def __init__(self, revo):
        print(revo[::-1])

ReverseIter(list(map(int, input().split())))   