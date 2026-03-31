a = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계"))
if a == 1:
    expr = input("수식을 입력하시오")
    result = eval(expr)
    print(f"{expr}{result}")

elif a == 2:
    num1 = int(input("첫번째 수 입력"))
    num2 = int(input("두번째 수 입력"))
    sig = 0
    for i in range(num1, num2 + 1):
        sig += i
    print(f"{num1}부터{num2}까지의 합은{sig}입니다")
else:
    print("1또는 2를 입력해야합니다")