#list of dictionary
company=[{'name':'amy','age':23,'salary':75000,'dept':'HR'},
         {'name':'ben','age':22,'salary':42000,'dept':'AM'},
         {'name':'chad','age':25,'salary':33000,'dept':'sales'}]
#print each dict one by one
for i in company:
    print(i)
print("---------------------")

#amy,ben,chad 
for i in company:
    print(i["name"])
print("---------------------")

#chad,ben,amy
for i in range(-1,-4,-1):
    print(company[i]['name'])
print("---------------------")

