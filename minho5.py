import math
n = float(input("반지름을 입력하세요 : "))
S = 4*math.pi*math.pow(n ,2)
V = 4/3*math.pi*math.pow(n ,3)
print("겉면적은 {}이고, 부피는 {}입니다. ".format(S , V))