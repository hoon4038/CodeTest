
list = []
cycle = int(input())
for _ in range(cycle):
    command = input()
    if command == "top":
        if len(list) == 0:  #리스트가 비워져 있을떼 -1 출력후 다음 반복문이 실행되도록 한다!! (아니면 print(list[-1] index 에러 발생)
            print(-1)
        else:
            print(list[-1])
    elif "push" in command:
        list.append(int(command[5:]))
    elif command == "pop":
        if len(list) == 0:   #리스트가 비워져 있을때 -1 출력 꼭 만들어 두기!!
            print(-1)
        else:
            print(list[-1])
            list.pop()
    elif command == "size":
        print(len(list))
    elif command == "empty":
        if len(list) != 0:
            print(0)
        else:
            print(1)