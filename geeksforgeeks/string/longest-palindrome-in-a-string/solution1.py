def is_palindrome(input_str):    
    size = len(input_str)
    if size == 1:
        return True

    middle = size // 2
    
    for i in range(middle):
        if input_str[i] != input_str[size-1-i]:
            return False

    return True


def get_longest_palindrome(input_str):    
    size = len(input_str)

    while size > 0:
        start = 0
        end = size

        while end <= len(input_str):
            if is_palindrome(input_str[start:end]):
                return input_str[start:end]

            start += 1
            end += 1

        size -= 1


def main():
    test_case = int(input())

    for _ in range(test_case):
        input_str = input()
        print(get_longest_palindrome(input_str))



if __name__ == "__main__":
    main()