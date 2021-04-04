# looping statements
# While And For Loops


'''
break => completly termincates the loop
continue => just skip the loop once
'''

i = 0
# while i <= 10: # True
#     if i == 5: break
#     print(str(i)+" >>> Hello world")
#     i = i + 1

j = 0
while j <= 10: # True
    j = j + 1
    if j == 5: continue
    if j == 8: continue
    #print(str(j)+" >>> Hello world")


votersList = ["Sai","Vicky","Honey","Gopi","Elon"]
votersList2 = ["Sai2","Vicky2","Honey2","Gopi2","Elon2"]

# break, continue
for name in votersList:
    print(name)
else:
    print("voter list has printed")

for vote in votersList:
    for vote2 in votersList2:
        print("Vote : "+vote+"\nVote2 : "+vote2)


# for x in range(19,90,5):
#     print(x)


    
    

