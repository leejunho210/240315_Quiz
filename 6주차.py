a = int(input("몇 단까지 출력할까요?:"))

for b in range(1,a+1):
    print("------[",b,"단]------")
    for c in range(1,20):
        print(b,"x",c,"=",ssb*c)