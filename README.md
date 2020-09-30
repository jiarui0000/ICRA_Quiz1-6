# ICRA_Quiz1-6

#Class SimplePendulum

Methods:

1. __init__(startPoint_x, startPoint_y, frequency)

Develop a simple pendulum. The horizontal distance between its initial position and the fixed point is x, and the vertical distance is y. The parameter "frequency" is the refresh frequency of the model corresponding to reality. The higher the frequency, the higher the accuracy and the longer the calculation time required. 

2. setFrenquncy(frequency)

Change the refresh rate. 

3. reset()

Reset the simple pendulum to the origional status. 

4. moveThroughTime()

Let the model refresh once. 

5. getCurrentX()

Return current x coordinate.

6. getCurrentY()

return current y coordinate.

7. getCurrentSituation()

Return a tuple with (velocity, runtime, x coordinate, y coordinate) of current status.

8. printCurrentSituation()

Print the current velocity, runtime, x and y coordinate. 

9. getSituationWithX(target_x)

Get the motion state for the specified x coordinate. Return a tuple with (velocity, runtime, x coordinate, y coordinate) of target status.

10. getSituationWithY(target_y)

Get the motion state for the specified y coordinate. Return a tuple with (velocity, runtime, x coordinate, y coordinate) of target status.

11. getSituationWithTime(target_time)

Get the motion state for the specified running time. Return a tuple with (velocity, runtime, x coordinate, y coordinate) of target status.