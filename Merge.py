class Merge:
    @staticmethod
    def sort(arr):
        aux = [0] * len(arr)
        Merge._sort(arr, aux, 0, len(arr) - 1)

    @staticmethod
    def _sort(arr, aux, l, r):
        if r <= l:
            return
        mid = l + (r - l) // 2
        Merge._sort(arr, aux, l, mid)
        Merge._sort(arr, aux, mid+1, r)
        Merge._merge(arr, aux, l, mid, r)

    # merge two subarray of arr
    # arr[l -> mid] and arr[mid+1 -> r]
    @staticmethod
    def _merge(arr, aux, l, m, r):
        for i in range(l, r + 1):
            aux[i] = arr[i]

        i, j, k = l, m + 1, l

        while i <= m and j <= r:
            if aux[i] < aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                j += 1
            k += 1
        
        while i <= m:
            arr[k] = aux[i]
            i += 1
            k += 1
