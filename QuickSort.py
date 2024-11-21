import random

class QuickSort:
	"""
	Implements the QuickSort algorithm.

	Methods:
		sort(arr): Public method to sort an array in-place.
		_sort(arr, lo, hi): Internal method for recursive Quicksort.
		_choose_pivot(arr, lo, hi): Selects a pivot for partitioning.
		_partition(arr, lo, hi): In-place partitioning.
	"""
	@staticmethod
	def sort(arr: list) -> None:
		"""
		Public method to sort the array.
		Args:
			arr(list): The array to be sorted
		"""
		if not arr:
			return
		QuickSort._sort(arr, 0, len(arr) - 1)


	@staticmethod
	def _sort(arr: list, lo: int, hi: int) -> None:
		"""
    	Recursively sorts the array in-place using the QuickSort algorithm.

    	Args:
        	arr (list): The array to be sorted.
        	lo (int): The starting index of the current partition.
        	hi (int): The ending index of the current partition.

    	Returns:
        	None: The array is modified in place.
    	"""
		if lo >= hi:
			return
		QuickSort._choose_pivot(arr, lo, hi)	
		ind = QuickSort._partition(arr, lo, hi)
		QuickSort._sort(arr, lo, ind - 1)
		QuickSort._sort(arr, ind + 1, hi)


	@staticmethod
	def _choose_pivot(arr: list, lo: int, hi: int) -> None:
		"""
		Chooses a pivot and swaps it with arr[lo]
		Args:
			arr (list): The array being sorted.
			lo (int): The starting index of the partition.
			hi (int): The ending index of the partition.
		"""
		random_ind = random.randint(lo, hi)
		arr[lo], arr[random_ind] = arr[random_ind], arr[lo]


	@staticmethod
	def _partition(arr: list, lo: int, hi: int) -> int:
		"""
		Partitions the array around the pivot (initially at index 'lo')

		Args:
			arr (list): The array to partition.
			lo (int): The starting index of the partition
			hi (int): The ending indeex of the partition

		Returns: 
			int: the final index of the pivot after partitioning.

		Time Complexity: O(n)
		Space Complexity: O(1)
		"""
		i = lo + 1
		pivot = arr[lo]
		for j in range(lo + 1, hi + 1):
			if arr[j] < pivot:
				arr[i], arr[j] = arr[j], arr[i]
				i += 1
		arr[i - 1], arr[lo] = arr[lo], arr[i - 1]

		return i - 1