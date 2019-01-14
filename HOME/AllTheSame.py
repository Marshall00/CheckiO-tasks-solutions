from typing import List, Any
#Set contains only unique values so this is quite efficient way to check whether all values are the same
#and not unique at the same time

def all_the_same(elements: List[Any]) -> bool:
    s=set()
    for element in elements:
        s.add(element)
    return len(s)==1 or len(s)==0
