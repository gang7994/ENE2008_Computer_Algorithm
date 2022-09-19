# 01 별모양 출력하기

def print_star(n):
    if n >0:
        print("*"*n)
        print_star(n-1)

print_star(5)