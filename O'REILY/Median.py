from typing import List

def checkio(data: List[int]) -> [int, float]:

    x=sorted(data)
    y=len(x)

    if y%2==0:
        a=(y/2)
        b=((y/2)-1)
        return (x[int(a)]+x[int(b)])/2
    else:
        a=(y-1)/2
        return x[int(a)]
