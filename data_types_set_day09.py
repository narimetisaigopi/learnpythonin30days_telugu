
#definition: stores in unordered, unindexed, changable and not allows duplicates

names = {"Sai","Gopi","Vamsi","Vinay","Sai"}   #set
names2 = {"8","3","2","2","2"}   #set

# for x in names:
#     print(x)
names.add("Divya") # single add
names.update({"Ramu","vinnil"}) #multiple add
#names.remove("sasas") #returns error if item not found
names.discard("Ramu") # remove to give error
# del names

names.union(names2)

print(names.union(names2))



