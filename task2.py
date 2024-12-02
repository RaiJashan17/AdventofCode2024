left_numbers=[]
right_numbers=[]
with open("task1input.txt", "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_numbers.append(left)
        right_numbers.append(right)
score=0
values={}
for num in left_numbers:
    values[num]=0
for num in right_numbers:
    if num in values:
        values[num]+=1
for i in values:
    score+=i*values[i]
print(score)
