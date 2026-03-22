# 진수 입력
NUM = int(input("입력 진수 결정(16/10/8/2) : "))

# 값 입력 (문자열로 받기)
Num = input("값 입력하기 : ")

# 입력된 진수 기준으로 10진수로 변환
num = int(Num, NUM)

# 결과 출력
print("16진수 ==> ", hex(num))
print("10진수 ==> ", num)
print("8진수 ==> ", oct(num))
print("2진수 ==> ", bin(num))
