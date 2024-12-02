left_numbers=[]
right_numbers=[]
with open("task1input.txt", "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_numbers.append(left)
        right_numbers.append(right)
distance=0
lowest={left:[-1,10000000000],right:[-1,100000000000]}
counter=len(left_numbers)
while counter>0:
    for i in range(0,len(left_numbers)):
        if left_numbers[i] < lowest[left][1] and left_numbers[i] != -1:
            lowest[left]=[i,left_numbers[i]]
    for i in range(0,len(right_numbers)):
        if right_numbers[i] < lowest[right][1] and right_numbers[i] != -1:
            lowest[right]=[i,right_numbers[i]]
    distance+=abs(lowest[left][1]-lowest[right][1])
    left_numbers[lowest[left][0]]=-1
    right_numbers[lowest[right][0]] = -1
    lowest[left]=[-1,10000000000]
    lowest[right]=[-1,100000000000]
    counter-=1
print(distance)

