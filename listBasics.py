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
MyList.append(list)
print(MyList)


#add  by position
MyList.insert(1,"banana")
print(MyList)