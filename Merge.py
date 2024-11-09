class Merge:
    @staticmethod
    def sort(arr: list[int]) -> None:
        Merge._sort(arr, 0, len(arr) - 1)

    @staticmethod
    def _sort(arr: list[int], l: int, r: int) -> None:
        if r <= l:
            return
        mid = l + (r - l) // 2
        Merge._sort(arr, l, mid)
        Merge._sort(arr, mid+1, r)
        Merge._merge(arr, l, mid, r)

    # merge two subarray of arr
    # arr[l -> mid] and arr[mid+1 -> r]
    @staticmethod
    def _merge(arr: list[int], l: int, m: int, r: int) -> None:
        n1, n2 = m - l + 1, r - m
        aux1 = [0] * n1
        aux2 = [0] * n2
        for i in range(0, n1):
            aux1[i] = arr[l + i]

        for j in range(0, n2):
            aux2[j] = arr[m + j + 1]

        i, j, k = 0, 0, l

        while i < n1 and j < n2:
            if aux1[i] < aux2[j]:
                arr[k] = aux1[i]
                i += 1
            else:
                arr[k] = aux2[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = aux1[i]
            i += 1
            k += 1
        
        while j < n2:
            arr[k] = aux2[j]
            j += 1
            k += 1