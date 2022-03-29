n = int(input("수를 입력하세요: "))
a=1
for i in range(1 , n+1):
    a *= i
print("1부터 n사이의 수의 곱은 {} 입니다".format(a))