def main():
    test_case = int(input())

    for t in range(test_case):
        sentence = input().split(".")
        
        for i in range(len(sentence)-1, -1, -1):
            print(sentence[i], end="")

            if i > 0:
                print(".", end="")
            else:
                print("")

if __name__ == "__main__":
    main()