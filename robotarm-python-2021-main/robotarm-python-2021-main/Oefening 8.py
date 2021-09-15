## Oefening 8
from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for i in range(0,7):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()