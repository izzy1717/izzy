def a():
    print("speed")
    distance = float(input("how far was it ?"))
    time = float(input("how long did it take?"))
    speed = distance * time
    print(speed)


def b():
    print("area")
    length = float(input("what is the length?"))
    breadth = float(input("what is the breadth?"))
    area = length * breadth
    print(area)


def c():
    print("pressure")
    force = float(input("what is the force?"))
    area = float(input("what is the area?"))
    pressure = force/area
    print(pressure)

def d():
    print("energy: potental energy")
    mass = float(input("what is the mass?"))
    gravity = float(input("what is the gravity?"))
    height = float(input("what is the height"))
    energy = mass*gravity*height
    print(energy)

def e():
    print("rectangular prism: volume")
    length = float(input("what is the length?"))
    width = float(input("what is the width?"))
    height = float(input("what is the height?"))
    rectangular = length*width*height
    print(rectangular)

def main():
     choice = input("what question do you want to perform :")
     if choice == "a":
         a()
     elif choice == "b":
         b()
     elif choice == "C":
         c()
     elif choice == "d":
         d()
     elif choice == "e":
         e()
     else:
         print('invalid input')


if __name__ == '__main__':
    main()