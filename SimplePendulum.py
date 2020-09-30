import math


class SimplePendulum:
    startPoint_x = 0.0  # (m)
    statePoint_y = 0.0  # (m) fix point height - ball height
    currentPoint_x = 0.0  # (m)
    currentPoint_y = 0.0  # (m) fix point height - ball height
    velocity = 0.0  # (m/s)
    theta = 0.0  # (rad) angle between the rope and the vertical
    acc = 0.0  # (m/s^2) rotate
    ropeLength = 0.0  # (m)
    accOfGravity = 9.8  # (m/s^2) downside
    frequency = 0.0  # (Hz)
    runtime = 0.0  # (s)

    def __init__(self, startPoint_x, startPoint_y, frequency):
        self.runtime = 0.0
        self.startPoint_x = startPoint_x
        self.startPoint_y = startPoint_y
        self.frequency = frequency
        self.currentPoint_x = startPoint_x
        self.currentPoint_y = startPoint_y
        self.theta = math.atan(abs(self.currentPoint_x / self.currentPoint_y))
        self.ropeLength = math.sqrt(startPoint_x * startPoint_x + startPoint_y * startPoint_y)
        self.velocity = 0.0
        self.acc = 0.0
        return

    def accelerationCalculate(self):
        self.acc = self.accOfGravity * math.sin(self.theta)
        return

    def velocityCalculate(self):
        self.accelerationCalculate()
        self.velocity += self.acc / self.frequency
        #print(self.velocity)
        return

    def positionCalculate(self):
        self.velocityCalculate()
        self.currentPoint_x -= self.velocity * math.cos(self.theta) / self.frequency
        self.currentPoint_y += self.velocity * math.sin(self.theta) / self.frequency
        self.theta = math.atan(self.currentPoint_x / self.currentPoint_y)
        # self.getCurrentSituation()
        self.errorCorrection()
        return

    def errorCorrection(self):
        error_length = math.sqrt(self.currentPoint_x * self.currentPoint_x + self.currentPoint_y * self.currentPoint_y)
        self.currentPoint_x = self.currentPoint_x * self.ropeLength / error_length
        self.currentPoint_y = self.currentPoint_y * self.ropeLength / error_length

    def getCurrentSituation(self):
        print('The line velocity is %.4f ' % self.velocity)
        print('The time cost is %.4f ' % self.runtime)
        print("x = %.7f" % self.currentPoint_x)
        print("y = %.7f" % self.currentPoint_y)
        print("l = %.7f" % math.sqrt(self.currentPoint_x * self.currentPoint_x + self.currentPoint_y * self.currentPoint_y))
        return

    def getVelocityWithX(self, target_x):
        self.runtime = 0.0
        while (abs(self.currentPoint_x - target_x) > 0.01):
            self.runtime += 1 / self.frequency
            self.positionCalculate()
        print("Get Velocity With X")
        self.getCurrentSituation()
        return

    def getVelocityWithY(self, target_y):
        self.runtime = 0.0
        while (abs(self.currentPoint_y - target_y) > 0.01):
            self.runtime += 1 / self.frequency
            self.positionCalculate()
        print("Get Velocity With Y")
        self.getCurrentSituation()
        return

    def getVelocityWithTime(self, target_time):
        self.runtime = 0.0
        while (abs(self.runtime - target_time) > 0.000001):
            self.runtime += 1 / self.frequency
            self.positionCalculate()
        print("Get Velocity With Time")
        self.getCurrentSituation()
        return


b = SimplePendulum(40, 30, 200000)
b.getVelocityWithX(-10)
b = SimplePendulum(40, 30, 200000)
b.getVelocityWithY(48.988)
b = SimplePendulum(40, 30, 200000)
b.getVelocityWithTime(4.261)
