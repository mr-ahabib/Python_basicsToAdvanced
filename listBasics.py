#List is denoted by []



MyList=["Apple","Mango", "Banana","Strawberry","Goava"]
print(MyList)


#length
print(len(MyList))
print(type(MyList))


#list access
print(MyList[1])
print(MyList[-1])

print(MyList[2:5])



#change item
MyList[3]="Date"
print(MyList)

#multi change
MyList[2:4]=["Kiwi", "Avocado"]
print(MyList)

#adding list items more

MyList.append("Banana")
print(MyList)


#multi list add
list=["Date","Strawberry","Olive"]
MyList.extend(list)
print(MyList)


#add  by position
MyList.insert(1,"banana")
print(MyList)


#tuple into list
list1=("Date","Strawberry","Olive")
MyList.extend(list1)
print(MyList)



# Remove List
MyList.remove("banana")
print(MyList)

#Remove by id
MyList.pop(1)
print(MyList)


#clear list content
list1=["Date","Strawberry","Olive"]
list1.clear()
print(list1)


#loop list

for x in MyList:
        print(x)




#List comprenhension
newlist=[]
for x in MyList:
        if "d" in x:
               newlist.append(x)

print(newlist) 



#sort list

MyList.sort()
print(MyList) 

numlist=[1,5,0,100,12,34,21,83,21,13]
numlist.sort()
print(numlist)

#descending order
numlist.sort(reverse=True)
print(f"Descending order: {numlist}")


#copy list
numlist1=numlist.copy()
print(numlist1)

#join list
Final_list=numlist+numlist1
print(Final_list)