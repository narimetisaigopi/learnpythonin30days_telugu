#definition: stores in unordered, indexed, changable and not allows duplicates and these are keys and values

myDict = {
    "key": "value",
   "title" :"Sai Gopi",
   "age" :25,
   'valid' : False
}

# for x,y in myDict.items():
#     print(x+" >>> "+str(y))

myDict['age'] = 17

myDict.pop("valid") #delete
myDict.clear()
del myDict
print(myDict)