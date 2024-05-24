class BungeoBbang:
    def __init__(self, contents, price):
        self.contents = contents
        self.price = price
        self.total_sales = 0

    def sell(self):
        self.total_sales += self.price
        print(f"{self.contents} 붕어빵이 {self.price}원에 판매되었습니다")


    def eat(self):
        print(f"{self.contents} 붕어빵을 먹었습니다.")


shu_bun = BungeoBbang("슈크림",2000)
shu_bun.sell()
print(f"총 판매금: {shu_bun.total_sales}원")

pat_bun = BungeoBbang("팥", 1000)
pat_bun.sell()
print(f"총 판매금: {pat_bun.total_sales}원")