'''
    to calculate number of all inversions in a given array
    say arr = [1, 2, 5, 4, 3]
    the inversion is the pair arr[i], arr[j]
    where i < j, but arr[i] > arr[j]
'''
class Inversion:
    # brute force method
    # Time Complexity: O(n^2)
    @staticmethod
    def cal_inversion(a: list[int]):
        count = 0
        for i in range(len(a)):
            for j in range(i, len(a)):
                if a[i] > a[j]:
                    print(f"Found an Inversion: [{a[i]}, {a[j]}]")
                    count += 1
        return count

    '''
        _____Divide and Conquer Method______
        Gist: Divide the given array at mid,
        which create three types of inversions
            left inversion: all inversions that are in left subarray
            right inversion: all inversions that are in right subarray
            split inversion: inversions that are split between the two subarray
        we will recursively calculate left, right and split inversion 
        then return their sum

        Time Complexity: O(n log(n))
        Space Complexity: O(n)
    '''
    @staticmethod
    def count_inv(a: list[int]):
        arr = [0] * len(a)
        for i in range(len(a)):
            arr[i] = a[i]
        return Inversion._sort_inv(arr, 0, len(arr) - 1)

    @staticmethod
    def _sort_inv(a: list[int], lo, hi):
        if lo >= hi:
            return 0
        mid = lo + (hi - lo) // 2
        x = Inversion._sort_inv(a, lo, mid)
        y = Inversion._sort_inv(a, mid+1, hi)
        z = Inversion._count_merge(a, lo, mid, hi)

        return x + y + z

    @staticmethod
    def _count_merge(a: list[int], lo, mid, hi):
        count = 0
        n1, n2 = mid - lo + 1, hi - mid

        left = [0] * n1
        for i in range(0, n1):
            left[i] = a[i + lo]

        right = [0] * n2
        
        for j in range(0, n2):
            right[j] = a[j + mid + 1]
    
        i, j, k = 0, 0, lo
        while i < n1 and j < n2:
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
                count += n1 - i
            k += 1

        while i < n1:
            a[k] = left[i]
            i += 1
            k += 1

        while j < n2:
            a[k] = right[j]
            j += 1
            k += 1

        return count
    