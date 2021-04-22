# 팔린드롬 문제 설명
# "토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 팔린드롬(palindrome)이라고 부릅니다. 문자열 word가 팔린드롬인지 확인하는 함수 is_palindrome를 쓰세요. is_palindrome은 word가 팔린드롬이면 True를, 팔린드롬이 아니면 False를 리턴합니다.

# 주의 사항
# 반드시 for문을 사용하셔야 합니다.
# append, insert 메소드와 del 함수를 사용하면 안됩니다.
# 자동 채점 과제이기 때문에, 문제의 조건에 정확히 따라주시기 바랍니다. 띄어쓰기도 일치해야 합니다.

###내가 짠 코드
def is_palindrome(word):
    # 코드를 입력하세요.
    for i in range(len(word)//2):
        if word[i] == word[len(word) - i - 1]:
            pass
        else:
            return False
    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))