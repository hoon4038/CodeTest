## 숫자 3개 뽑기
from random import randint

def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

## 숫자 예측하기 [내가 짠 코드]
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    count = 1
    while count < 4:
        guess = int(input("{0}번째 숫자를 입력하세요: ".format(count)))
        if guess in new_guess:
            print("중복되는 숫자 입니다. 다시 입력하세요.")
        elif guess < 0 or guess > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif guess not in new_guess:
            new_guess.append(guess)
            count += 1

    return new_guess

## 숫자 예측하기 [해설]
def take_guess2():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        new_num = int(input("{0}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))
        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_num)

    return new_guess

# print(take_guess2())
# 조건문에 범위 벗어나는것 먼저 적용하자! 추가하는것 적용하면 밑에 elif / else 진행을 안해서 중복 및 범위 벗어난것도 추가됨!

## 점수계산
def get_score(guess, solution):
    strike_count = 0
    ball_count = 0
    for n in range(0, 3):
        if guess[n] == solution[n]:
            strike_count += 1
        elif guess[n] in solution:
            ball_count += 1

    return strike_count, ball_count

ANSWER = generate_numbers()
tries = 0

#내가 짠 코드
while True:
    tries += 1
    guess = take_guess()
    s_c , b_c = get_score(guess, ANSWER)
    if s_c != 3:
        print("{0}S {1}B".format(s_c, b_c))
    else:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))

# guess를 반복문안에서 초기화 해주어야 다음 try로 넘어간다 아니면 무한루프에 빠진다!

## 해설
# while True:
#     user_guess = take_guess2()
#     s, b = get_score(user_guess, ANSWER)
#
#     print("{}S {}B\n".format(s, b))
#     tries += 1
#     if s == 3:
#         break
#
# print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
