# Heap Sort using MaxHeap 

def heapify(arr, N, i):
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2	
  
	if l < N and arr[largest] < arr[l]:
		largest = l

	if r < N and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] 
		heapify(arr, N, largest)


def heapSort(arr):
	N = len(arr)
	# Generating the maxHeap
	for i in range(N//2 - 1, -1, -1):
		heapify(arr, N, i)
	# adding the elements in the array
	for i in range(N-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] 
		heapify(arr, i, 0)

arr = [15,13,2,25,7,20,8,4]
heapSort(arr)
print(arr)

  
