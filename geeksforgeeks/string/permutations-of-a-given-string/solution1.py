def main():
    test_case = int(input())

    for _ in range(test_case):
        str_input = input()
        for permutation in get_all_permutation(str_input):
            print(permutation, end=" ")
        print("")


def get_all_permutation(s: str):
    s = "".join(sorted(s))
    return _permutation(s)    


def _permutation(s: str):
    if len(s) == 1:
        return [s]
    elif len(s) == 2:
        return [s, s[1]+s[0]]
    else:   
        result = []     
        for i in range(len(s)):
            permutation_list = _permutation(s[0:i] + s[i+1:])            
            permutation_list = map(lambda x: s[i] + x, permutation_list)
            for permutation in permutation_list:
                result.append(permutation)
        
        return result


if __name__ == "__main__":
    main()