x_y = list(input("Enter the coords (x,y): ").split(","))
for x,y in enumerate(x_y):
    if x_y[x].startswith("("):
        x_y[x] = y.replace("(","")
    if x_y[x].endswith(")"):
        x_y[x] = y.replace(")","")
dist = (int(x_y[0])**2 + int(x_y[1])**2)**0.5
if dist <= 10:
    print("The dart is within the board")
else:
    print("The dart is outside the board")
