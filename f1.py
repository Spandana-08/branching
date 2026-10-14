#NESTED_LIST

employes=[["raksh",23,40000],["adithi",48,78000],["ambhi",33,35000]]
#iterate and print each inner list one by one
for employe in employes:
    print(employe)
#iterate and print names one by one
for employe in employes:
    print(employe[0])
#salary
for employe in employes:
    print(employe[2])
#iterate and print the names of employess whose age is greater than 32 and salary less than 64000
for employee in employes:
    if employee[1]>32 and employee[2]<64000:
        print(employee[0])

    
# example
for i in range(2,-1,-1):
    print(employes[i][0])
   

    
       

        
