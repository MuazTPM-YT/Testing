fly_coords = (5,5)
body_coords = (10,10)

shot = (input("Enter the coords: ")).split(",")

if int(shot[0]) == fly_coords[0] and int(shot[-1]) == fly_coords[-1]:
    print("You hit the fly")

elif int(shot[0]) <= body_coords[0] and int(shot[-1]) <= body_coords[-1]:
    print("You hit the body")
    
elif int(shot[0]) > body_coords[0] and int(shot[-1]) > body_coords[-1]:
    print("You hit nothing")

else:
    print("Invalid")