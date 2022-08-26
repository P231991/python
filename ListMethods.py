list1 = ["python","stats","NLP","ML","DL"]
list2 = [10, 20, 60 ,30, 70, 40, 20, 50]
list3 = [True, False, True, False]
list4 = [100, "Python", True]
list5 = []
print("list1=",list1,'of type(list1)=',type(list1),"and len(list1) is",len(list1))
print("list2=",list2,'of type(list2)=',type(list2),"and len(list2) is",len(list2))
print("list3=",list3,'of type(list3)=',type(list3),"and len(list3) is",len(list3))
print("list4= {0} of type(list4)= {1} and len(list4) is {2}".format(list4,type(list4),len(list4)))
print("list5= {0} of type(list5)= {1} and len(list5) is {2}".format(list5,type(list5),len(list5)))
print("========================")
# list.append({element/item}) - To add element to the list
print("Method 1. list.append({element/item}) - To add element to the list")
print("original list5=",list5)
list5.append("RR") # adding RR to list5
list5.append("RCB")# adding RCB to list5
list5.append("MI") # adding MI to list5
list5.append("Chennai")# adding Chennai to list5
print("list5 after appending items=",list5, "len(list5)=",len(list5))
list5.append(list4) # adding list4 to list5
print("list5 after appending list4=",list5, "len(list5)=",len(list5))
list5.append(list3) # adding list3 to list5
print("list5 after appending list3=",list5, "len(list5)=",len(list5))
list5.append(list2) # adding list2 to list5
print("list5 after appending list2=",list5, "len(list5)=",len(list5))
print("=======================")
print("List Slicing")
print("list5[0]=",list5[0])
print("list5[1]=",list5[1])
print("list5[2]=",list5[2])
print("list5[3]=",list5[3])
print("list5[4]=",list5[4])
print("list5[4][0]=",list5[4][0])
print("list5[4][1]=",list5[4][1])
print("list5[4][2]=",list5[4][2])
print("list5[5]=",list5[5])
print("list5[5][0]=",list5[5][0])
print("list5[5][1]=",list5[5][1])
print("list5[6]=",list5[6])
print("list5[6][0]=",list5[6][0])
print("list5[6][1]=",list5[6][1])
print("list5[6][2]=",list5[6][2])
print("list5[6][3]=",list5[6][3])
print("list5[0:4]=",list5[0:4])
print("list5[-3:]=",list5[-3:])
print("=======================")
# 2. list.extend({element/list}) - To add list to the existing list - output is only 1 list
print("Method 2. list.extend({element}) - To add list to the existing list - output is only 1 list")
print("list4=",list4)
print("len(list4)=",len(list4))
print("list3=",list3)
print("len(list3)=",len(list3))
list4.extend(list3)
print("list4 after extending list3=",list4)
print("len(list4)=",len(list4))
list4.extend(list2)
print("list4 after extending list2=",list4)
print("len(list4)=",len(list4))
list4.extend(list1)
print("list4 after extending list1=",list4)
print("len(list4)=",len(list4))
list4.extend(["Python"])
print("list4=",list4)
print("==============================")
# 3. list.insert(index, element) - TO add element to the specific index position of the list using index
print("Method 3. list.insert(index, element) - TO add element to the specific index position of the list using index")
print("list3=", list3)
print("len(list3)=", len(list3))
list3.insert(1,"IPL")
print('list3.insert(1,"IPL")')
print("list3=", list3)
print("len(list3)=", len(list3))
list3.insert(2,"Python")
print('list3.insert(2,"Python")')
print("list3=", list3)
print("len(list3)=", len(list3))
list3.insert(3, list2)
print('list3.insert(3,list2)')
print("list3=", list3)
print("len(list3)=", len(list3))
list3.insert(-1,"IPL")
print("======================")
# 4. list.pop({index}) - To remove element using index. If you don't pass index, then it will remove last element
print("Method 4. list.pop({index}) - To remove element using index. If you don't pass index, then it will remove last element")
print("list3=",list3,"of len(list3)",len(list3))
list3.pop()
print("list3.pop() - Remove last element from the list")
print("list3=",list3,"of len(list3)",len(list3))
list3.pop(-2)
print("list3.pop(-2) -  Remove element at index: -2")
print("list3=",list3,"of len(list3)",len(list3))
print("======================")
# 5. list.remove({element}) - To remove elements from the list
print("Method 5. list.remove({element}) - To remove elements from the list")
print("list3=",list3,"of len(list3)",len(list3))
list3.remove("IPL")
print('list3.remove("IPL")')
print("list3=",list3,"of len(list3)",len(list3))
print("======================")
# 6. list.count({element}) - TO count the number of occurance of an element
print("Method 6. list.count({element}) - TO count the number of occurance of an element")
print("list4=",list4)
print("list4.count(True)=",list4.count(True))
print("list4.count(False)=",list4.count(False))
print("list4.count('Python')=",list4.count("Python"))
print("list4.count(20)=",list4.count(20))
print("list4.count('DL')=",list4.count('DL'))
print("======================")
# 7. list.index({element}) - TO get the index position of an element
print("Method 7. list.index({element}) - TO get the index position of an element")
print("list3=",list3)
print("len(list3)=",len(list3))
print("list3.index(True)=",list3.index(True))
print("list3.index(False)=",list3.index(False))
print("list3.index('Python')=",list3.index('Python'))
print("list3.index('IPL')=",list3.index('IPL'))
print("=======================")
# 8. list.reverse() - To reverse the sequence of the list
print("Method 8. list.reverse() - To reverse the sequence of the list")
print("list1=",list1)
list1.reverse()
print("list1.reverse()")
print("list1 after reverse=",list1)
print("=======================")
# 9. list.sort()
print("list2=",list2)
list2.sort() # By default sort() will sort element in ascending order 
print("list2.sort()=",list2)
list2.sort(reverse=True)
print("list2.sort(reverse=True)=",list2)
print("=======================")
# 10. list.copy() - To create deep copy object
print("Method 10. list.copy() - To create deep copy object")
list6 = list1
print("list6 = list1")
print("list1 =",list1)
print("list6 =", list6)
list1.pop()
list1.pop()
print("After list1.pop()")
print("list1 =",list1)
print("list6 =", list6)
print('--------------')
print("list7 = list1.copy()")
list7 = list1.copy()
print("list1 =",list1)
print("list7 =", list7)
list1.pop()
print("After list1.pop()")
print("list1 =",list1)
print("list7 =", list7)
print("=======================")
# 11. list.clear() - To clear all elements in the list
print("Method 11. list.clear() - To clear all elements in the list")
print("list1=",list1)
list1.clear()
print("list1=",list1)
print("=======================")
# del is used to delete the list
del list1
print("list1=",list1)


