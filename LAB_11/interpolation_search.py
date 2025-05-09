def interpolation_search(arr, key):
  low = 0
  high = len(arr) - 1
  while low <= high and arr[low] <= key <= arr[high]:
     pos = low + ((key - arr[low]) * (high - low) // (arr[high] - arr[low]))
     if arr[pos] == key:
       return pos
     elif arr[pos] < key:
       low = pos + 1
     else:
        high = pos - 1
  return -1
arr = [10,20,30,40,50]
key = 30
print("Element found at index:", interpolation_search(arr, key))
