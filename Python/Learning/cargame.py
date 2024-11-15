name=input("What is your name?: ")
engine, motion = False, False
while True:
    command = input("> ").lower()
    if command == "help": 
        print(f"On: Starts the car\nOff: Stops the engine\nGo: The car moves forward\nStop: The car stops\nR: Car turns right\nL: Car turns left\nExit: Quit the game")
    elif command == "on":
        if engine == True: 
            print("The care is already on")
        else:
            print("The car has started")
            engine = True
    elif command == "off":
        if motion == False:
            if engine == False: 
                print("The car is already off")
            else:
                print("The car is off")
                engine = False
        else: 
            print("Stop da car first bru")
    elif command == "go":
        if engine == True:
            print("The car is going")
            motion = True
        else: 
            print("The car won't be able to move")
    elif command == "stop":
        if engine == True:
            if motion == True: 
                print("The car has stopped")
                motion = False
            else: 
                print("The car is already stationary")
        else: 
            print("The car is already stopped if the engine wasn't on")
    elif command == "r":
        if engine == True:
            if motion == True: 
                print("The car turned right")
            else: 
                print("The car is not moving")
        else: 
            print("What car can go right if it aint even on?")
    elif command == "l":
        if engine == True:
            if motion == True: 
                print("The car turned left")
            else: 
                print("The car is not moving")
        else: 
            print("What car can go right if it aint even on?")
    elif command == "exit":
        print("Bye ")
        break
    else: 
        print("That is not a command! Type `help` if you need the list of commands")