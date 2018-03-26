# projectile.py

"""projectile.py
Provides a simple class for modeling the
flight of projectiles."""
import math

class Projectile:

    """Simulates the flight of simple prohectiles near the earth's
        surface, ignoring wind resistance.  Tracking is done in two
        dimensions,height (y) and distance (x)."""

    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        self.xpos = 0.0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    def getX(self):
        "Returns the y position (height) of this projectile."
        return self.xpos

    def getY(self):
        "Returns the x position (distance) of this projectile."
        return self.ypos

    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1)/2.0
        self.yvel = yvel1


def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input("Enter teh time interval between position calculations: "))

    return a,v,h,t

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))

if __name__ == "__main__":
    main()
