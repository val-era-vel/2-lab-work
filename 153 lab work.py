x1 = int(input("Введіть координату х:"))
y1 = int(input("Введіть координату у:"))
if x1>0 and y1>0 :
    print("I чверть")
elif x1>0 and y1<0 :
    print("IV чверть")    
elif x1<0 and y1>0 :
    print("II чверть")   
elif x1<0 and y1<0 :
    print("III чверть")    
else:
    print("Такої чверті немає")



    