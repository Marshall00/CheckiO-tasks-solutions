from typing import List
import math #importing math cause 'acos' (arc cosinus) needed to calculate angles

def checkio(a: int, b: int, c: int) -> List[int]:
    angles=[]
    degree_indicator=57.2957795 #fixed value to convert radians to degrees
    if (a+b)>c and (a+c)>b and (b+c)>a: #condition - traingle possible to be built or not (?)

        angle_A=math.acos((b**2+c**2-a**2)/(2*b*c))     #Pure mathematical formulas
        angles.append(round(angle_A*degree_indicator))

        angle_B=math.acos((a**2+c**2-b**2)/(2*a*c))
        angles.append(round(angle_B*degree_indicator))

        angle_C=math.acos((a**2+b**2-c**2)/(2*a*b))
        angles.append(round(angle_C*degree_indicator))

    else:
        return [0,0,0]

    return sorted(angles)