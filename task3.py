result=0
with open("task3input.txt", "r") as file:
    for line in file:
        array = [int(num) for num in line.split()]
        pointer1 = 1
        pointer2 = 2
        flag=0
        if array[0] < array[1] < array[0]+4:
            flag=1
        elif array[1] <array[0] < array[1]+4:
            flag=2
        if flag==1:
            while pointer2 < len(array):
                if not array[pointer1] < array[pointer2] < array[pointer1]+4:
                    flag=0
                pointer1+=1
                pointer2+=1
        if flag==2:
            while pointer2 < len(array):
                if not array[pointer2] < array[pointer1] < array[pointer2]+4:
                    flag=0
                pointer1+=1
                pointer2+=1
        if flag!=0:
            result+=1
print(result)