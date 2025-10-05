n = int(input("Введіть число від 128 до 255: "))

binary = format(n, "08b")   

if binary == binary[::-1]:
    print("True")
else:
    print("False")



    


