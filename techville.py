def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def enter_roundabout():
    print("entering the roundabout")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

start_engine()

destination = input("Where do you want to go? ")

if destination == "library":
    move_forward()
    turn("left")
    print("we arrived at the library!")

elif destination == "tech park":
    move_forward()
    turn("right")
    print("we arrived at tech park!")

elif destination in ["hospital", "mall", "airport", "university", "stadium"]:
    move_forward()
    enter_roundabout()

    if destination == "hospital":
        follow_roundabout(1)
        print("we arrived at the hospital!")

    elif destination == "mall":
        follow_roundabout(2)
        move_forward()
        turn("right")
        print("we arrived at the mall!")

    elif destination == "airport":
        follow_roundabout(3)
        print("we arrived at the airport!")

    elif destination in ["university", "stadium"]:
        follow_roundabout(4)
        move_forward()

        if destination == "university":
            turn("left")
            print("we arrived at the university!")
        else:  # destination == "stadium"
            turn("right")
            print("we arrived at the stadium!")

else:
    print("invalid destination")

stop_engine()
