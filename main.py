import random

src=open("municipalities.txt","r")
addressFile=open("addressFinal.txt", "r")
municipalities=[]
costs=[]
address=[]
roomsAr=[1,2,3,4,5,6,7]
roomsArMost=[3,4,5,6,7]
pplArMost=[2,3,4,5,6]
pplAr=[1,2,3,4,5,6,7,8]
apartment=[]
dedicated=[]
view=[]
dfm=[]
# INITS
for line in src:
    municipalities.append(line)
for i in range(1,800):
    costs.append(round(random.uniform(8.3,73.2),2))
for i in range(1,200):
    costs.append(round(random.uniform(56.2,373.2),2))
random.shuffle(costs)
for line in addressFile:
    address.append(line)
for i in range (0,197):#if garden or pool is one, append zero
    val=round(pow(random.choice([2.9,0,0,0,0,3.8,4.4,5.6,6.9,3.2,8,5.4,9.4]),random.choice([2.1,3.4,1.8,1.6,1.9,2.3])))
    if val==1:
        dedicated.append(0)
    else
        dedicated.append(val)
    val=round(pow(random.choice([2.9, 0, 4.4, 0, 2,3.5, 3.2, 0, 0 , 0 , 0 , 0 , 5.4 ]), random.choice([1.7,1.9,2.1])))
    if val==1:
        dedicated.append(0)
    else
        dedicated.append(val)
    dedicated.append(random.choice(["No","Yes","No","No"]))
for i in range(0,300):
    apartment.append(random.choice([0,1,2,3,4,5,6,7,8]))
    apartment.append(random.choice([True, False]))
    apartment.append(random.choice([True, False]))
for i in range (0,498):
    view.append(random.choice(["Road", "Sea", "Mountain"]))








