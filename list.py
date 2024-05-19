#list - linear ordered mutable(changeable) w/c accepts duplicate values
list1 = [3,6,9,12,15]
list1.append(25)
list1.insert(1,15)

print("1", list1)
list1.reverse()
print("2", list1)
list1.sort()
print("3", list1) #ascending order
list1.sort(reverse=True) #descending order
print("4", list1)

list1.remove(15)
print("5", list1)
list1.remove(15)
print("6", list1)


#data structure - collection of certain values
#STACK: First In, Last Out
#QUEUE: First in First Out
#to add member append()
#to come out: pop(0)

#copy()
list2 = list1
list3 = list1.copy()
list1.append(99)
print(7, "List 1: ",list1)
list2.append(88)
print(8, "List 2: ",list2)
list3.append(66)
print(8, "List 3: ",list3)