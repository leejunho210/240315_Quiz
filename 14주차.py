foodmenu = ["1. 냉면", "2. 볶음밥", "3. 피자", "4. 짜장면"]

try:
    choose = int(input("원하는 메뉴의 숫자를 입력하세요: "))
    if choose < 1 or choose > 4:
        raise IndexError

    selected_menu = foodmenu[choose - 1]
    print((selected_menu) + "을 선택하셨습니다.")


except ValueError:
    print("숫자만 입력 가능합니다. ")

except IndexError:
    print("해당 번호에 할당된 음식이 없습니다.")