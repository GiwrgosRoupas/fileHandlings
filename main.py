import random

src=open("municipalities.txt","r")
addressFile=open("address.txt", "r")
municipalities=[]
costs=[]
address=[]
rooms=[1,2,3,4,5,6,7]
ppl=[1,2,3,4,5,6,7,8]

# INITS
for line in src:
    municipalities.append(line)
for i in range(1,800):
    costs.append(round(random.uniform(8.3,73.2),2))
for i in range(1,200):
    costs.append(round(random.uniform(56.2,373.2),2))
for line in addressFile:
    address.append(line)






