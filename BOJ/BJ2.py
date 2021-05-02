import sys
n = int(input())

for i in range(n):
    sentence = list(sys.stdin.readline().split()) #문장을 리스트로 입력받는다
    for j in sentence: #리스트 안에서 하나 씩 뒤집어 주자
        print(j[::-1], end=" ")  #end=" "를 써서 단어하나를 뒤집고 띄어쓰기하도록
