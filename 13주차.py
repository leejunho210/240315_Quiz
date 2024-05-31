class Beverage:
    # 클래스 속성으로 음료 메뉴와 가격을 딕셔너리로 정의
    menu = {'커피': 3000, '녹차': 2500, '아이스티': 3000}

    @staticmethod
    def calculate(name, quantity):
        # 입력된 음료의 가격을 수량과 곱하여 총 가격을 계산
        if name in Beverage.menu:
            return Beverage.menu[name] * quantity
        else:
            return None

def run_kiosk():
    print("환영합니다. 음료를 선택해 주세요.")
    for drink, price in Beverage.menu.items():
        print(f"{drink}: {price}원")

    # 사용자로부터 음료 이름 입력받기
    selected_beverage = input("음료를 선택하세요: ")

    if selected_beverage not in Beverage.menu:
        print("선택하신 음료가 메뉴에 없습니다.")
        return

    try:
        # 사용자로부터 음료 수량 입력받기
        quantity = int(input("수량을 입력하세요: "))
        if quantity <= 0:
            print("수량은 1 이상의 값을 입력해야 합니다.")
            return
    except ValueError:
        print("유효한 수량을 입력하세요.")
        return

    # 선택한 음료의 총 가격을 계산
    total_price = Beverage.calculate(selected_beverage, quantity)
    if total_price is not None:
        print(f"총 가격은 {total_price}원 입니다.")

# 키오스크 프로그램 실행
run_kiosk()
