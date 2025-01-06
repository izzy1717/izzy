def a():
    print("speed")
    distance = float(input("input distance:"))
    time = float(input("input time:"))
    speed = distance * time
    print(speed)


def b():
    print("area")
    length = float(input("input length:"))
    width = float(input("input width:"))
    heigth = float(input("input heigth:"))
    volume = length * width * heigth
    print(volume)


def c():
    print("pressure")
    force = float(input("input force:"))
    area = float(input("input area:"))
    pressure = force/area
    print(pressure)

def d():
    print("energy: potental energy")
    mass = float(input("input mass:"))
    gravity = float(input("input gravity:"))
    height = float(input("input height:"))
    energy = mass*gravity*height
    print(energy)

def e():
    print("rectangular prism: volume")
    length = float(input("input length:"))
    width = float(input("input width:"))
    height = float(input("input height:"))
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