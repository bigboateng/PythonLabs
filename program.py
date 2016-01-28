

rho = 1.204
v = 30*30
while True:
    numbers = input("Enter lift, drag, surface: ")
    try:
        liftForce = float(numbers.split(',')[0])
        dragForce = float(numbers.split(',')[1])
        surfaceArea = float(numbers.split(',')[2])
        print("The lift force is :::::" + str(liftForce))
        print("The drag force is :::::" + str(dragForce))
        print("The surface area force is ::::" + str(surfaceArea))
        print("**************************")
        cl = (2.0*liftForce)/(rho*v*surfaceArea)
        cd = (2.0*dragForce)/(rho*v*surfaceArea)
        # L = 0.5*rho*v^2*S*Cl
        # D = 0.5*rho*v^2*S*Cd
        d = 1.225
        print("Cl = " + str(cl) + "  |||||| cd = " + str(cd))
        print("**************************")
        print("\n")
    except IndexError:
        print("ERROR! MAKE SURE YOU ENTER 3 VALUES")
        print("\n")

