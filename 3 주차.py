환율 = {"달러" : 1320, "엔" : 950, "위안" : 182}

money = [13, 200, 13]
a = money[0] * 환율["달러"]
b = money[1] * 환율["엔"]
c = money[2] * 환율["위안"]

d = "철수가 가지고 있는 돈의 원화 가치는 원 입니다"
e = (a+b+c)
f = "원 입니다"

print(d, e, f)