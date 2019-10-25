class Solution:
	def sortArray(self, nums: List[int]) -> List[int]:
		# self.quickSort(nums, 0, len(nums) - 1)
		# self.mergeSort(nums)
		# self.bubbleSort(nums)
		# self.insertionSort(nums)
		# self.selectionSort(nums)
		self.heapSort(nums)
		return nums
	
	# @bubbleSort, TLE
	def bubbleSort(self, nums):
		n = len(nums)
		for i in range(n):
			for j in range(0, n - i - 1):
				if nums[j] > nums[j + 1]:
					nums[j], nums[j + 1] = nums[j + 1], nums[j]
					
	# @insertionSort, TLE
	def insertionSort(self, nums): 
		for i in range(1, len(nums)): 
			key = nums[i]
			j = i-1
			while j >= 0 and key < nums[j] : 
					nums[j + 1] = nums[j] 
					j -= 1
			nums[j + 1] = key
		
	# @selectionSort, TLE
	def selectionSort(self, nums):
		for i in range(len(nums)):
			_min = min(nums[i:])
			min_index = nums[i:].index(_min)
			nums[i + min_index] = nums[i]
			nums[i] = _min
		return nums
	
	# @quickSort
	def quickSort(self, nums, low, high):
		def partition(nums, low, high):
			i = low - 1
			pivot = nums[high]

			for j in range(low , high):
				if nums[j] <= pivot: 
					i = i + 1 
					nums[i], nums[j] = nums[j], nums[i] 

			nums[i+1], nums[high] = nums[high], nums[i+1] 
			return i + 1
		
		if low < high:
			pi = partition(nums, low, high) 

			self.quickSort(nums, low, pi-1)
			self.quickSort(nums, pi+1, high)
	 
	 # @mergeSort
	
	def mergeSort(self, nums): 
		if len(nums) > 1: 
			mid = len(nums)//2
			L = nums[:mid] 
			R = nums[mid:] 

			self.mergeSort(L)
			self.mergeSort(R)

			i = j = k = 0

			while i < len(L) and j < len(R): 
				if L[i] < R[j]: 
					nums[k] = L[i] 
					i+=1
				else: 
					nums[k] = R[j] 
					j+=1
				k+=1
 
			while i < len(L): 
				nums[k] = L[i] 
				i+=1
				k+=1

			while j < len(R): 
				nums[k] = R[j] 
				j+=1
				k+=1
   
   # @heapSort
	def heapSort(self, nums):
		def heapify(nums, n, i): 
			largest = i
			l = 2 * i + 1
			r = 2 * i + 2
			
			if l < n and nums[i] < nums[l]: 
				largest = l 

			if r < n and nums[largest] < nums[r]: 
				largest = r 

			if largest != i: 
				nums[i], nums[largest] = nums[largest], nums[i]
				
				heapify(nums, n, largest)
				
		n = len(nums) 

		for i in range(n, -1, -1): 
			heapify(nums, n, i) 

		for i in range(n-1, 0, -1): 
			nums[i], nums[0] = nums[0], nums[i]
			heapify(nums, i, 0) 