from SimplePendulum import SimplePendulum

b = SimplePendulum(40, 30, 200000)
print(b.getSituationWithX(-10))
print(b.getSituationWithY(48.988))
print(b.getSituationWithTime(4.2615))
print("x= ", b.getCurrentX(), ", y= ", b.getCurrentY())
