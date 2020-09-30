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
        self.__runtime = 0.0
        self.__startPoint_x = startPoint_x
        self.__startPoint_y = startPoint_y
        self.__frequency = frequency
        self.__currentPoint_x = startPoint_x
        self.__currentPoint_y = startPoint_y
        if self.__currentPoint_y != 0:
            self.__theta = math.atan(abs(self.__currentPoint_x / self.__currentPoint_y))
        else:
            self.__theta = math.pi / 2
        self.__ropeLength = math.sqrt(startPoint_x * startPoint_x + startPoint_y * startPoint_y)
        self.__velocity = 0.0
        self.__acc = 0.0
        return

    def setFrenquncy(self, frequency):
        self.__frequency = frequency
        return

    def reset(self):
        self.__runtime = 0.0
        self.__currentPoint_x = self.__startPoint_x
        self.__currentPoint_y = self.__startPoint_y
        self.__theta = math.atan(abs(self.__currentPoint_x / self.__currentPoint_y))
        self.__velocity = 0.0
        self.__acc = 0.0
        return

    def __accelerationCalculate(self):
        self.__acc = self.__accOfGravity * math.sin(self.__theta)
        return

    def __velocityCalculate(self):
        self.__accelerationCalculate()
        self.__velocity += self.__acc / self.__frequency
        #print(self.velocity)
        return

    def __positionCalculate(self):
        self.__velocityCalculate()
        self.__currentPoint_x -= self.__velocity * math.cos(self.__theta) / self.__frequency
        self.__currentPoint_y += self.__velocity * math.sin(self.__theta) / self.__frequency
        self.__theta = math.atan(self.__currentPoint_x / self.__currentPoint_y)
        # self.getCurrentSituation()
        self.__errorCorrection()
        return

    def moveThroughTime(self):
        self.__runtime += 1 / self.__frequency
        self.__positionCalculate()
        return

    def __errorCorrection(self):
        error_length = math.sqrt(self.__currentPoint_x * self.__currentPoint_x + self.__currentPoint_y * self.__currentPoint_y)
        self.__currentPoint_x = self.__currentPoint_x * self.__ropeLength / error_length
        self.__currentPoint_y = self.__currentPoint_y * self.__ropeLength / error_length
        return

    def getCurrentX(self):
        x = self.__currentPoint_x
        return x

    def getCurrentY(self):
        y = self.__currentPoint_y
        return y

    def getCurrentSituation(self):
        v = self.__velocity
        r = self.__runtime
        x = self.__currentPoint_x
        y = self.__currentPoint_y
        return v, r, x, y

    def printCurrentSituation(self):
        print('The line velocity is %.4f ' % self.__velocity)
        print('The time cost is %.4f ' % self.__runtime)
        print("x = %.7f" % self.__currentPoint_x)
        print("y = %.7f" % self.__currentPoint_y)
        # print("l = %.7f" % math.sqrt(self.currentPoint_x * self.currentPoint_x + self.currentPoint_y * self.currentPoint_y))
        return

    def getSituationWithX(self, target_x):
        self.reset()
        while abs(self.__currentPoint_x - target_x) > 0.0001:
            self.moveThroughTime()
        print("Get Velocity With X")
        t = self.getCurrentSituation()
        return t

    def getSituationWithY(self, target_y):
        self.reset()
        while abs(self.__currentPoint_y - target_y) > 0.0001:
            self.moveThroughTime()
        print("Get Velocity With Y")
        t = self.getCurrentSituation()
        return t

    def getSituationWithTime(self, target_time):
        self.reset()
        while abs(self.__runtime - target_time) > 0.000001:
            self.moveThroughTime()
        print("Get Velocity With Time")
        t = self.getCurrentSituation()
        return t

