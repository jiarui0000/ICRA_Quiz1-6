import math


class SimplePendulum:
    __startPoint_x = 0.0  # (m)
    __statePoint_y = 0.0  # (m) fix point height - ball height
    __currentPoint_x = 0.0  # (m)
    __currentPoint_y = 0.0  # (m) fix point height - ball height
    __velocity = 0.0  # (m/s)
    __theta = 0.0  # (rad) angle between the rope and the vertical
    __acc = 0.0  # (m/s^2) rotate
    __ropeLength = 0.0  # (m)
    __accOfGravity = 9.8  # (m/s^2) downside
    __frequency = 0.0  # (Hz)
    __runtime = 0.0  # (s)

    def __init__(self, startPoint_x, startPoint_y, frequency):
        self.runtime = 0.0
        self.startPoint_x = startPoint_x
        self.startPoint_y = startPoint_y
        self.frequency = frequency
        self.currentPoint_x = startPoint_x
        self.currentPoint_y = startPoint_y
        self.theta = math.atan(abs(self.__currentPoint_x / self.__currentPoint_y))
        self.ropeLength = math.sqrt(startPoint_x * startPoint_x + startPoint_y * startPoint_y)
        self.velocity = 0.0
        self.acc = 0.0
        return

    def reset(self):
        self.runtime = 0.0
        self.currentPoint_x = startPoint_x
        self.currentPoint_y = startPoint_y
        self.theta = math.atan(abs(self.currentPoint_x / self.currentPoint_y))
        self.velocity = 0.0
        self.acc = 0.0
        return

    def __accelerationCalculate(self):
        self.acc = self.accOfGravity * math.sin(self.theta)
        return

    def __velocityCalculate(self):
        self.accelerationCalculate()
        self.velocity += self.acc / self.frequency
        #print(self.velocity)
        return

    def __positionCalculate(self):
        self.velocityCalculate()
        self.currentPoint_x -= self.velocity * math.cos(self.theta) / self.frequency
        self.currentPoint_y += self.velocity * math.sin(self.theta) / self.frequency
        self.theta = math.atan(self.currentPoint_x / self.currentPoint_y)
        # self.getCurrentSituation()
        self.__errorCorrection()
        return

    def __moveThroughTime(self):
        self.runtime += 1 / self.frequency
        self.positionCalculate()
        return

    def __errorCorrection(self):
        error_length = math.sqrt(self.currentPoint_x * self.currentPoint_x + self.currentPoint_y * self.currentPoint_y)
        self.currentPoint_x = self.currentPoint_x * self.ropeLength / error_length
        self.currentPoint_y = self.currentPoint_y * self.ropeLength / error_length
        return

    def getCurrentSituation(self):
        print('The line velocity is %.4f ' % self.velocity)
        print('The time cost is %.4f ' % self.runtime)
        print("x = %.7f" % self.currentPoint_x)
        print("y = %.7f" % self.currentPoint_y)
        print("l = %.7f" % math.sqrt(self.currentPoint_x * self.currentPoint_x + self.currentPoint_y * self.currentPoint_y))
        return

    def getSituationWithX(self, target_x):
        self.reset()
        while (abs(self.currentPoint_x - target_x) > 0.001):
            self.__moveThroughTime()
        print("Get Velocity With X")
        self.getCurrentSituation()
        return

    def getSituationWithY(self, target_y):
        self.reset()
        while (abs(self.currentPoint_y - target_y) > 0.001):
            self.__moveThroughTime()
        print("Get Velocity With Y")
        self.getCurrentSituation()
        return

    def getSituationWithTime(self, target_time):
        self.reset()
        while (abs(self.runtime - target_time) > 0.000001):
            self.__moveThroughTime()
        print("Get Velocity With Time")
        self.getCurrentSituation()
        return

