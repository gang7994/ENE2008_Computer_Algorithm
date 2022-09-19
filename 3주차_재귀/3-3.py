# 03 진수 변환하기(재귀)
def convert_B(x, n):
    if n < x:
        print(arr[n], end="")
    else:
        convert_B(x, n//x)
        print(arr[n%x], end="")
arr = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

n = int(input("10진수 입력 : "))

print("2진수 : ", end="")
convert_B(2, n)
print("\n8진수 : ", end="")
convert_B(8, n)
print("\n16진수 : ", end="")
convert_B(16, n)