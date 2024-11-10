'''
    to calculate number of all inversions in a given array
    say arr = [1, 2, 5, 4, 3]
    the inversion is the pair arr[i], arr[j]
    where i < j, but arr[i] > arr[j]
'''
class Inversion:
    @staticmethod
    # brute force method
    def cal_inversion(a: list[int]):
        count = 0
        for i in range(len(a)):
            for j in range(i, len(a)):
                if a[i] > a[j]:
                    print(f"Found an Inversion: [{a[i]}, {a[j]}]")
                    count += 1
        return count