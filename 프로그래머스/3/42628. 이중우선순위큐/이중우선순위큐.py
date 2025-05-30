import heapq

def solution(operations):
    min_heap = []  
    max_heap = []  

    for op in operations:
        command, num = op.split()
        num = int(num)

        if command == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)

        elif command == "D":
            if num == -1 and min_heap:  
                min_value = heapq.heappop(min_heap)
                max_heap.remove(-min_value)
                heapq.heapify(max_heap)
                
            elif num == 1 and max_heap:
                max_value = -heapq.heappop(max_heap)
                min_heap.remove(max_value)
                heapq.heapify(min_heap)

    if not min_heap:
        return [0, 0]

    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
