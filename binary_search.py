array = [1, 5, 14, 16, 19]
def binary_search(array, key):
	ini = 0
	fim = len(array) 
	while ini < fim:
		mid = (ini + fim)/2

		if key > array[mid]:
			ini = mid + 1
		elif key < array[mid]:
			fim = mid - 1
		else:
			return mid
	return -1


# test if 19 is in array
print binary_search(array, 5)

# another case

def binary_search_recursive(array, key, ini, fim):

	mid = (ini + fim)/2

	if ini > fim:
		return -1 
	if key < array[mid]:
		return binary_search_recursive(array, key, ini, mid - 1)
	elif key > array[mid]:
		return binary_search_recursive(array, key, mid+1, fim)
	else:
		return mid
	return -1

print binary_search_recursive(array, 12, 0, len(array))