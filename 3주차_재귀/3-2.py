# 02 진수 변환하기(비재귀)

def convert_A(x,n):
    tmp = []
    while n >= 0:
        if n < x:
            tmp.append(arr[n])
            break
        else:
            tmp.append(arr[n%x])
            n//=x
    for i in range(len(tmp)-1,-1, -1):
        print(tmp[i], end='')

        
arr = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]


n = int(input("10진수 입력 : "))
print("\n2진수:", end='')
convert_A(2,n)
print("\n8진수:", end='')
convert_A(8,n)
print("\n16진수:", end='')
convert_A(16,n)

