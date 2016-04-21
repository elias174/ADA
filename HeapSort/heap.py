from math import floor

def Left(index):
	return 2 * index

def Right(index):
	return (2 * index) + 1

def Parent(index):
	floor(index / 2)

def MaxHeapify(tree, size, index):
	left = Left(index)
	right = Right(index)
	print left, right
	if left <= size and tree[left] > tree[index]:
		largest = left
	else:
		largest = index
	if right <= size and tree[right] > tree[largest]:
		largest = right
	if largest != index:
		tree[index], tree[largest] = tree[largest], tree[index]
		MaxHeapify(tree, size, largest)

def BuildMaxHeap(tree):
	k = (len(tree)/2 )-1
	while k>0:
		MaxHeapify(tree,len(tree),k)
		k -= 1


def Sort(items):
	BuildMaxHeap(items)
	size = len(items)
	for i in range(len(items) - 1, 0, -1):
		items[0], items[i] = items[i], items[0]
		MaxHeapify(items, size-1, 1)
	return items

def main():
	li = [0, 16, 4, 10, 1, 23]
	print Sort(li)


main()
