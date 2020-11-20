from itertools import permutations

def main():
    test_case = int(input())

    for _ in range(test_case):
        str_input = input()
        for permutation in get_all_permutation(str_input):
            print(permutation, end=" ")
        print("")


def get_all_permutation(s: str):
    s = "".join(sorted(s))
    return ["".join(p) for p in permutations(s)]
    

if __name__ == "__main__":
    main()