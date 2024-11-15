x_y_z = list(input("Enter the coords (x,y,z): ").split(","))
for x,z in enumerate(x_y_z):
    if x_y_z[x].startswith("("):
        x_y_z[x] = z.replace("(","")
    if x_y_z[x].endswith(")"):
        x_y_z[x] = z.replace(")","")
dist = ((0-int(x_y_z[0]))**2 + (0-int(x_y_z[1]))**2 + (0-int(x_y_z[2]))**2)**0.5
print(dist)
if dist <= 17.33:
    if 8.66 <= dist <= 8.67:
        print("You shot the fly!")
    else:
        print("You missed the fly!")
else:
    print("Your aim sucks")