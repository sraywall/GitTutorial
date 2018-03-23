# cball2.py
import math

def getInputs():
    angle = float(input("Enter the launch angle (in degrees): "))
    vel = float(input("Enter the intitial velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))
    return angle, vel, h0, time

def getXYComponents(vel, angle):
     # convert angle to radians
    theta = (math.pi * angle) / 180
    theta = math.radians(angle)
    yvel = vel * math.sin(theta)
    xvel = vel * math.cos(theta)

    return xvel, yvel
   
def updateCannonBall(time,xpos,ypos,xvel,yvel):
    xpos = xpos + time * xvel
    yvel1 = yvel - time * 9.8
    ypos += time * (yvel + yvel1)/2.0
    yvel = yvel1
    
    return xpos, ypos, yvel


def main():
    angle, vel, h0, time = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    # loop until the ball hits the ground
    while ypos >= 0.0:
        xpos, ypos, yvel = updateCannonBall(time, xpos, ypos, xvel, yvel)
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

if __name__ == "__main__":
    main()
