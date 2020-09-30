# ICRA_Quiz1-6

#Class SimplePendulum
Methods:

1. __init__(startPoint_x, startPoint_y, frequency)
Develop a simple pendulum. The horizontal distance between its initial position and the fixed point is x, and the vertical distance is y. The parameter "frequency" is the refresh frequency of the model corresponding to reality. The higher the frequency, the higher the accuracy and the longer the calculation time required

2. reset()
Reset the simple pendulum to the origional status

3. getCurrentSituation()
Print the current velocity, runtime, x and y coordinate

4. getSituationWithX(target_x)
Get the motion state for the specified x coordinate

5.getSituationWithY(target_y)
Get the motion state for the specified y coordinate

6. getSituationWithTime(target_time)
Get the motion state for the specified running time