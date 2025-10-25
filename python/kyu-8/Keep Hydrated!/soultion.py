import math
def litres(time):
    result = time * 0.5
    result = math.floor(result)
    return result

#or
def litres(time):
    return int(time*0.5)
