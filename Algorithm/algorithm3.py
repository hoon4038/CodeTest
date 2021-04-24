## 내가 짠 코드
def binary_search(element, some_list):
    # 코드를 작성하세요.
    start_index = 0
    end_index = len(some_list) - 1
    binary_index = (start_index + end_index) // 2

    while binary_index != 0:
        binary_index = (start_index + end_index) // 2
        if element == some_list[binary_index]:
            return binary_index

        elif element > some_list[binary_index]:
            start_index = binary_index
            if start_index == end_index - 1:
                start_index = end_index
            else:
                continue
        elif element < some_list[binary_index]:
            end_index = binary_index
            if start_index == end_index - 1:
                end_index = start_index
            else:
                continue
    return None


## 해설
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))