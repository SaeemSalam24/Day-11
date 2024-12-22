
def linear_search(arr, target):
    
    for i in range(len(arr)):
        
        if arr[i] == target:
            return i
        
    return -1

arr = [23, 42, 8, 15, 7, 35]
target = 15

result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
