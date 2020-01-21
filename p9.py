import os
def dirTree(dir):
    for child in os.listdir(dir):
        path = os.path.join(dir, child)
        if os.path.isdir(path):
            print(path)
            dirTree(path)
        else:
            print('|--', child)


# dir = input()

dir = 'E:\\pyAssign\\'
dirTree(dir)
