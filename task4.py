def is_valid_sequence(arr):
    return all(abs(arr[i] - arr[i + 1]) <= 3 for i in range(len(arr) - 1))

def is_strictly_ascending(arr):
    return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)) and is_valid_sequence(arr)

def is_strictly_descending(arr):
    return all(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) and is_valid_sequence(arr)

def can_be_sorted_with_one_removal(arr):
    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i + 1:]
        if is_strictly_ascending(new_arr) or is_strictly_descending(new_arr):
            return True
    return False  

result=0
with open("task3input.txt", "r") as file:
    for line in file:
        array = [int(num) for num in line.split()]
        if can_be_sorted_with_one_removal(array):
            result+=1
print(result)