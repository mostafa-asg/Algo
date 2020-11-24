import heapq

def main():
    test_case = int(input())
    for _ in range(test_case):
        _ = input() # N
        arr = map(int, input().strip().split(" "))
        sorted_arr = sort_by_frequency(arr)
        for item in sorted_arr:
            print(item, end=" ")
        print("")


def sort_by_frequency(arr):
    item_freq = dict()
    freq = dict()

    for item in arr:
        old = item_freq.get(item, 0)    
        item_freq[item] = old + 1

    for k,v in item_freq.items():
        old_list = freq.get(v, [])
        old_list.append(k)
        freq[v] = old_list

    min_heap = []
    for k, v in freq.items():
        heapq.heappush(min_heap, (k*-1, v)) # multiply by -1 because it is min heap

    sorted_arr = []
    while len(min_heap) > 0:
        freq_num, l = heapq.heappop(min_heap)
        # convert to positive value
        freq_num = freq_num * -1

        for item in sorted(l):
            for _ in range(freq_num):
                sorted_arr.append(item)

    return sorted_arr


if __name__ == "__main__":
    main()