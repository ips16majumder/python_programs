
def bubble(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                swapped = True
                list[i], list[i+1] = list[i+1], list[i]
    return list

list1 = [9,8,7,6,5,4,22,54,11,1]
bubble(list1)
print(list1)
