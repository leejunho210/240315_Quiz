score_str = input("점수를 입력하세요: ")
score = int(score_str)  # 문자열을 숫자로 변환

if score <= 10:
    result = 'D'
elif score <= 40:
    result = 'C'
elif score <= 70:
    result = 'B'
else:
    result = 'A'

print(result)
