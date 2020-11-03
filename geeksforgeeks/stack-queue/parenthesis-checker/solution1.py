from collections import deque

opening = ["(", "[", "{"]
closing = [")", "]", "}"]
pairs = { close:open_ for close,open_ in zip(closing, opening) }

def main():
    t = int(input())

    for iter in range(t):
        line = input()
        stack = deque()
        balanced = True

        for ch in line:
            if ch in opening:
                stack.append(ch)
            elif ch in closing:
                try:
                    poped = stack.pop()
                    if pairs[ch] != poped:
                        balanced = False                           
                        break
                except IndexError:
                        balanced = False
                        break

        if len(stack) == 0 and balanced:
            print("balanced")
        else:
            print("not balanced")
             

if __name__ == "__main__":
    main()