#name=muskan kumari
#Roll no=2501010265
#Date=07 oct,2025
#Project:Building a calorie tracking console app

print("welcome to daily calorie tracker")
print("enter your daily calorie intake")
meal=[]
calorie=[]
no=int(input("enter the number of meal you ate"))
for i in range (no):
    m=(i+1)
    c=(i+1)
    m=input("enter meal name:")
    c=float(input("enter calorie:"))
    meal.append(m)
    print(meal)
    calorie.append(c)
    print(calorie)
    
print("\n---meal summary---")
print("meal name\tcalories")
print("----------------------")

for i in range(no):
    print(meal[i]," "*(15 -len(meal[i])),calorie[i])

total_calories=sum(calorie)
print("your total calorie are",total_calories)

average=(total_calories)
average=total_calories/no
print("your average calorie are",average)


daily_limit=float(input("enter daily limit calorie"))
if total_calories> daily_limit:
    print("warning")

else:
    print("success")

    print("control your calorie limit")

