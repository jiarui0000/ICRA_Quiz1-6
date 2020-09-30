import numpy
import math

class SimplePendulum:
    startPoint_x = 0.0 #(m)
    statePoint_y = 0.0 #(m) fix point height - ball height
    currentPoint_x = 0.0 #(m)
    currentPoint_y = 0.0 #(m) fix point height - ball height
    velocity = 0.0 #(m/s)
    theta = 0.0 #(rad) angle between the rope and the vertical
    acc = 0.0 #(m/s^2) rotate
    ropeLength = 0.0 #(m)
    accOfGravity = 9.8 #(m/s^2) downside
    frequency = 0.0 #(Hz)
    runtime = 0.0 #(s)


    def __init__(self, startPoint_x, startPoint_y, frequency):
        self.startPoint_x = startPoint_x
        self.startPoint_y = startPoint_y
        self.frequency = frequency
        self.currentPoint_x = startPoint_x
        self.currentPoint_y = startPoint_y
        self.theta = math.atan(abs(currentPoint_x / currentPoint_y))
        self.ropeLength = numpy.sqrt(numpy.square(startPoint_x) + numpy.square(startPoint_y))
        self.velocity = 0.0
        self.acc = 0.0
        return


    def accelerationCalculate(self):
        self.acc = accOfGravity * math.sin(theta)
        return

    def velocityCalculate(self):
        self.accelerationCalculate()
        self.velocity += self.acc / self.frequency
        return

    def positionCalculate(self):
        self.velocityCalculate()
        self.currentPoint_x -= self.velocity * math.cos(self.theta)
        self.currentPoint_y += self.velocity * math.sin(self.theta)
        self.theta = math.atan(currentPoint_x / currentPoint_y)
        return

    def getVelocityWithX(self, target_x):
        self.runtime = 0.0
        while (abs(self.currentPoint_x - target_x) > 0.00001) :
            self.runtime += 1/frequency
            positionCalculate()
        print('The line velocity is %.4f \n' % self.velocity)
        print('The time cost is %.4f \n' % self.runtime)
        return


b = SimplePendulum(0.3, 1, 30)
b.getVelocityWithX(0.1)
print "hello"
