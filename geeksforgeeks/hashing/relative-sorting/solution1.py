import heapq

def sort_relatively(arr1, arr2):
    first_part = {item:0 for item in arr2}
    last_part = []    
    
    for item in arr1:
        if item in first_part:
            value = first_part[item]
            first_part[item] = value + 1
        else:
            heapq.heappush(last_part, item)

    result = []
    for item in arr2:
        for _ in range(first_part[item]):
            result.append(item)

    while len(last_part) > 0:
        result.append(heapq.heappop(last_part))

    return result


def main():
    t = int(input())

    for _ in range(t):
        # N, M
        input()
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        
        result = sort_relatively(arr1, arr2)
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()