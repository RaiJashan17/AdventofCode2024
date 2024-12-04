import re

def extract_and_multiply(input_string):
    pattern = r'mul\((\d+),(\d+)\)'
    results = re.findall(pattern, input_string)
    return [int(x) * int(y) for x, y in results]

result=0
with open("task5input.txt", "r") as file:
    for line in file:
        arr = extract_and_multiply(line)
        result+=sum(arr)
print(result)