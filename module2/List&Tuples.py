#create list
fruits = ["apple", "banana", "orange", "banana", "banana"] 
print ("\nTHE ORIGINAL LIST : ", fruits)

#append method
fruits.append("mango") 
print("\nafter append method : ", fruits)

#copy
new_list = fruits.copy()
print ("\nafter copy method", new_list)

#count
count = fruits.count("banana")
print ("\ncount of banana : ", count)

#delete
del fruits[3]
print ("\nafter delete index 3 : ", fruits)

#extend - add multiple value
more_fruits = ["grape", "pear", "pineapple"]
fruits.extend(more_fruits)
print ("\nafter extend method : ", fruits)

#indexing
print ("\nindexing the element 1 : ", fruits[1])

#insert
fruits.insert(1, "cucumber")
print ("\nafter inserting cucumber to the index 1 : ", fruits)

#modify
fruits[2] = "dragonfruit"
print ("\nafter changing index 2 : ", fruits)

#pop
print ("\npop index 2 :", fruits.pop(2))
print ("after pop the index 2 : ", fruits)

#remove
print ("\nremove cucumber : ", fruits.remove("cucumber"))
print ("after removal -cucumber- : ", fruits)

#reverse
fruits.reverse()
print ("\nreverse version of the list :", fruits)

#slicing
print("\nafter slice 1 to 4 :", fruits[1:4]) 


print("\n")