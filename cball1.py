# cball1.py
import math
def main():
    angle = float(input("Enter the launch angle (in degrees): "))
    vel = float(input("Enter the intitial velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))

    # convert angle to radians
    theta = (math.pi * angle) / 180
    theta = math.radians(angle)

    # set the initial position and velocities in x and y directions
    xpos = 0.0
    ypos = h0
    yvel = vel * math.sin(theta)
    xvel = vel * math.cos(theta)

    # loop until the ball hits the ground
    while ypos >= 0.0:
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos += time * (yvel + yvel1)/2.0
        yvel = yvel1

    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

if __name__ == "__main__":
    main()
