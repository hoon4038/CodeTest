import sys
n = int(input())

for i in range(n):
    vps_problem = input()
    count = 0
    for i in range(len(vps_problem)):
        if vps_problem[i] == '(': # '('나 ')'를 받앗을때 count를 더하고 뺀다
            count += 1
        elif vps_problem[i] == ')': #')'를 받았을 때는 조건을 하나 더 붙여야함 ['('가 먼저 와야하기 때문]
            count -= 1
            if count < 0:
                break
            else:
                continue


    if count == 0:
        print('YES')
    elif count != 0:
        print('NO')