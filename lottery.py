# 번호 뽑기
# 내가 짠 코드
# from random import randint
#
# def generate_numbers(n):
#     num_list = []
#     for i in range(n+1):
#         a = randint(1,46)
#         if a in num_list:
#             while a in num_list:
#                 a = randint(1,46)
#         num_list.append(a)
#     return num_list
#
# print(generate_numbers(6))

#코드잇
# from random import randint
#
# def generate_numbers(n):
#     numbers = []
#     while len(numbers) < n:    #리스트갯수로 반복문을 사용할거면 len함수를 사용하자!
#         num = randint(1, 45)
#         if num not in numbers:
#             numbers.append(num)
#
#     return numbers
#
# print(generate_numbers(6))


# 당첨 번호 뽑기
# 내가 짠 코드
# from random import randint
#
# def generate_numbers(n):
#    numbers = []
#    while len(numbers) < n:
#        num = randint(1, 45)
#        if num not in numbers:
#            numbers.append(num)
#
#    return numbers
#
# def draw_winning_numbers():
#     winning_numbers = []
#     while len(winning_numbers) < 6:
#         win_num = randint(1, 45)
#         if win_num not in winning_numbers:
#             winning_numbers.append(win_num)
#         winning_numbers.sort()
#
#     bonus_num = randint(1, 45)
#     if bonus_num not in winning_numbers:
#         winning_numbers.append(bonus_num)
#
#     return winning_numbers
#
# print(generate_numbers(6))
# print(draw_winning_numbers())


#코드잇
#
# from random import randint
#
# def generate_numbers(n):
#    numbers = []
#    while len(numbers) < n:
#        num = randint(1, 45)
#        if num not in numbers:
#            numbers.append(num)
#
#    return numbers
#
# def draw_winning_numbers():
#     winning_numbers = generate_numbers(7)    #만들어 두었던 함수를 최대한 활용하자!
#     return sorted(winning_numbers[:6]) + winning_numbers[6:]  #리스트 슬라이싱을 해야 반환값이 리스트로 나온다!!!
#
#     리스트끼리 더해서 리스트를 만들자!
#
# print(draw_winning_numbers())

#겹치는 번호 개수
# def count_matching_numbers(list_1, list_2):
#     count = 0
#     for num in list_1:
#         if num in list_2:
#             count += 1
#
#     return count
# print(count_matching_numbers([1,2,3], [1]))

#당첨금 규칙
#내가 짠 코드
# def count_matching_numbers(numbers, winning_numbers):
#     count = 0
#     for num in numbers:
#         if num in winning_numbers:
#             count += 1
#
#     return count
#
# def check(numbers, winning_numbers):
#     if count_matching_numbers(numbers, winning_numbers) == 3:
#         return 5000
#     elif count_matching_numbers(numbers, winning_numbers) == 4:
#         return 50000
#     elif count_matching_numbers(numbers, winning_numbers) == 5:
#         return 1000000
#     elif count_matching_numbers(numbers, winning_numbers) == 6:
#         if winning_numbers[6] in numbers:
#             return 50000000
#         else:
#             return 100000000

#코드잇
from random import randint

def generate_numbers(n):
   numbers = []
   while len(numbers) < n:
       num = randint(1, 45)
       if num not in numbers:
           numbers.append(num)

   return numbers

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)    #만들어 두었던 함수를 최대한 활용하자!
    return sorted(winning_numbers[:6]) + winning_numbers[6:]  #리스트 슬라이싱을 해야 반환값이 리스트로 나온다!!!


def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1

    return count



def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])  # 1.참가자 번호 6개와 당첨번호 6개 중 몇개가 일치하는가
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])  # 2.참가자 번호 6개와 보너스 번호 1개 중 몇 개가 일치하는지
    if count ==6 :
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0