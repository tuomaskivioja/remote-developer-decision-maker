def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

destination = input("Where do you want to go? ")

start_engine()
move_forward()

if destination == "school":
    turn("right")
    print("we arrived at school!")
elif destination == "grocery store" or destination == "dentist":
    turn("left")
    move_forward()
    if destination == "grocery store":
        turn("right")
        print("we arrived at grocery store!")
    else:
        turn("left")
        print("we arrived at dentist!")
elif destination == "restaurant":
    move_forward()
    print("we arrived at restaurant!")
else:
    print("invalid destination")