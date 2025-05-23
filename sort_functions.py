class Sort():
    def __init__(self, array = []):
        self.array = array

    def __str__(self):
        return str(self.array)

    def _swap(self, a, b):
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp
    
    def bubble_sort(self):
        assert len(self.array) > 0
        done = False
        while not done:
            done = True
            for i in range(len(self.array)-1):
                if self.array[i] > self.array[i+1]:
                    done = False
                    self._swap(i, i+1)
    
    def selection_sort(self):
        assert len(self.array) > 0
        for i in range(len(self.array)):
            min_index = i
            min_val = self.array[i]
            for j in range(i, len(self.array)):
                if self.array[j] < min_val:
                    min_val = self.array[j]
                    min_index = j
            self._swap(min_index, i)
    
    def insertion_sort(self):
        assert len(self.array) > 0
        for i in range(1, len(self.array)):
            index = i
            while index > 0 and self.array[index] < self.array[index-1]:
                self._swap(index-1, index)
                index -= 1
            
    def binary_insertion_sort(self):
        assert len(self.array) > 0

        def binary_search(val, left, right):
            l, r = left, right
            while l < r:
                mid = (l+r)//2
                if self.array[mid] >= val:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        for i in range(1, len(self.array)):
            if (self.array[i-1] > self.array[i]):
                index = binary_search(self.array[i], 0, i)
                temp = self.array.pop(i)
                self.array = self.array[0:index] + [temp] + self.array[index::]

    def counting_sort(self):
        assert len(self.array) > 0
        min_val, max_val = min(self.array), max(self.array)
        offset = -1 * min_val
        count_range = max_val-min_val+1
        count = [0 for i in range(count_range)]
        for i in range(len(self.array)):
            count[self.array[i] + offset] += 1

        array_pos = 0
        count_pos = 0
        while array_pos < len(self.array):
            if count[count_pos] > 0:
                self.array[array_pos] = count_pos - offset
                array_pos += 1
                count[count_pos] -= 1
                continue
            count_pos += 1

    def merge_sort(self):
        def merge(s1, s2):
            i, j = 0, 0
            merged = []
            while i < len(s1) and j < len(s2):
                if s1[i] < s2[j]:
                    merged.append(s1[i])
                    i += 1
                else:
                    merged.append(s2[j])
                    j += 1
            merged.extend(s1[i::])
            merged.extend(s2[j::])
            return merged
        
        # Merge sort code starts here:
        assert len(self.array) > 0

        if len(self.array) == 1:
            return self.array
        
        subset = [[val] for val in self.array]

        while len(subset) > 1:
            merged = []
            
            pos = 0
            while pos < len(subset):
                if pos + 1 < len(subset):
                    merged.append(merge(subset[pos], subset[pos+1]))
                else:
                    merged.append(subset[pos])
                pos += 2
            subset = merged
        
        self.array = subset[0]

    def optimized_merge_sort(self):
        def merge(s1, s2):
            i, j = 0, 0
            merged = []
            while i < len(s1) and j < len(s2):
                if s1[i] < s2[j]:
                    merged.append(s1[i])
                    i += 1
                else:
                    merged.append(s2[j])
                    j += 1
            merged.extend(s1[i::])
            merged.extend(s2[j::])
            return merged
        
        # Merge sort code starts here:
        assert len(self.array) > 0

        if len(self.array) == 1:
            return self.array
        
        subset = [] # takes advantage of already-sorted subarrays
        tmp = [self.array[0]]
        for i in range(1, len(self.array)):
            if (self.array[i-1] > self.array[i]):
                subset.append(tmp)
                tmp = [self.array[i]]
            else:
                tmp.append(self.array[i])

        if (len(tmp) > 0):
            subset.append(tmp)

        while len(subset) > 1:
            merged = []
            
            pos = 0
            while pos < len(subset):
                if pos + 1 < len(subset):
                    merged.append(merge(subset[pos], subset[pos+1]))
                else:
                    merged.append(subset[pos])
                pos += 2
            subset = merged
        
        self.array = subset[0]
    
    def quick_sort(self):
        def partition(arr, piv):
            if (len(arr) == 0):
                return ([], [])
            
            left, right = partition(arr[1::], piv)

            if (arr[0] >= piv):
                right.append(arr[0])
            else:
                assert arr[0] < piv
                left.append(arr[0])

            return (left, right)
        
        def quicksort_helper(arr):
            if (len(arr) == 0):
                return []
            
            piv = arr[0]
            x, y = partition(arr[1::], piv)

            return quicksort_helper(x) + [piv] + quicksort_helper(y)
        
        # Quick sort code starts here
        assert len(self.array) > 0

        self.array = quicksort_helper(self.array)

    def shell_sort(self):
        assert len(self.array) > 0
        partition_size = len(self.array)//2
        while (partition_size > 0):
            for i in range(partition_size, len(self.array)):
                temp = i
                while (temp - partition_size >= 0 and self.array[temp] < self.array[temp-partition_size]):
                    self._swap(temp, temp-partition_size)
                    temp -= partition_size
            partition_size //= 2
    
    def heap_sort(self):
        import heapq
        assert len(self.array) > 0
        heap_array = self.array.copy()
        heapq.heapify(heap_array)
        result = []
        while (heap_array):
            result.append(heapq.heappop(heap_array))
        self.array = result

        
if __name__ == '__main__':
    # Bubble Sort 
    sort_test = Sort()
    sort_test.array = [0, -18, 20, -44, 39, 57, 4, 8, 9, -17]
    sort_test.bubble_sort()
    print(f"Bubble Sort Results: {sort_test}")

    # Selection Sort
    sort_test.array = [-57, 82, -36, 19, -65, 43, -91, 28, 75, -10]
    sort_test.selection_sort()
    print(f"Selection Sort Results: {sort_test}") 

    # Insertion Sort
    sort_test.array = [-8, 16, -3, 20, -12, 9, -5, 14, -7, 18]
    sort_test.insertion_sort()
    print(f"Insertion Sort Results: {sort_test}") 

    # Binary Insertion Sort
    sort_test.array = [-2, 6, -14, 9, -5, 12, -7, 4, -11, 8, -200, 132, 10, -1]
    sort_test.binary_insertion_sort()
    print(f"Binary Insertion Sort Results: {sort_test}") 

    # Counting Sort
    sort_test.array = [17, -3, 10, -6, 14, -9, 5, -12, 11, -1]
    sort_test.counting_sort()
    print(f"Counting Sort Results: {sort_test}") 

    # Merge Sort
    sort_test.array = [-16, 13, -8, 3, -10, 7, -15, 2, -4, 1]
    sort_test.merge_sort()
    print(f"Merge Sort Results: {sort_test}")

    # Optimized Merge Sort
    sort_test.array = [-16, 13, -8, 3, -10, 7, -15, 2, -4, 1]
    sort_test.optimized_merge_sort()
    print(f"Optimized Merge Sort Results: {sort_test}")

    # Quick Sort
    sort_test.array = [-16, 13, -8, 3, -10, 7, -15, 2, -4, 1]
    sort_test.quick_sort()
    print(f"Quick Sort Results: {sort_test}")

    # Shell Sort
    sort_test.array = [17, -3, 10, -6, 14, -9, 5, -12, 11, -1]
    sort_test.shell_sort()
    print(f"Shell Sort Results: {sort_test}") 

    # Heap Sort
    sort_test.array = [-16, 13, -8, 3, -10, 7, -15, 2, -4, 1]
    sort_test.heap_sort()
    print(f"Heap Sort Results: {sort_test}") 
