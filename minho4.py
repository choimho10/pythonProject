n = int(input("온도를 입력하세요: "))
a = input("입력하신 온도를 화씨(F)로 바꿀까요? 아니면 섭씨(C)로 바꿀까요 ? ")
c=0
d=0
if a == "F":
    c = (9/5)*n+32
    print("화씨로 바꾸면{}F 입니다 ".format(c))
elif a == "C":
    d = (5/9)*(n-32)
    print("섭씨로 바꾸면{}C 입니다 ".format(d))