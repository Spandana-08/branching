#NESTED_DICTINORY

company={
    'emp1':{'name':'amy','age':23,'salary':75000,'dept':'HR'},
    'emp2':{'name':'ben','age':22,'salary':42000,'dept':'AM'},
    'emp3':{'name':'chad','age':25,'salary':33000,'dept':'sales'}}
print(company)
print("------------------------------------")
for i in company:
    print(i)
print("------------------------------------")
# print outer key
for ok in company:
    print(company.get(ok))
print("------------------------------------")
#another method
for ok in company:
    print(company[ok])
print("------------------------------------")
#using value methods
for value in company.values():
    print(value)
print("------------------------------------")
# print amy,ben,chad
for ok in company:
    print(company[ok]['name'])
print("------------------------------------")
#another method
for value in company.values():
    print(value['name'])
print("------------------------------------")
for value in company.values():
    print(value.get('name'))
print("------------------------------------")
for value in company.values():
    print(value.get('salary'))
print("------------------------------------")
#print name of the emp whose salary is greater then 30000 and dept is sales
for value in company.values():
    if  value['salary']>30000 and value['dept']=="sales":
        print(value['name'])
