color1 = input("Введіть перший колір (blue, green, red): ").lower()
color2 = input("Введіть другий колір (blue, green, red): ").lower()
valid_colors = ["blue", "green", "red"]
if color1 not in valid_colors or color2 not in valid_colors:
    print("Такої палітри немає!")
elif color1 == color2:
    print("Ви ввели однакові кольори:", color1)
elif (color1 == "red" and color2 == "green") or (color1 == "green" and color2 == "red"):
    print("Жовтий")
elif (color1 == "blue" and color2 == "green") or (color1 == "green" and color2 == "blue"):
    print("Блакитний")
elif (color1 == "blue" and color2 == "red") or (color1 == "red" and color2 == "blue"):
    print("Magenta")


