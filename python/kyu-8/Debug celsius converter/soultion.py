def weather_info(temp):
    c = convert_to_celsius(temp) #python use "=" to assign value to variable.
    if c <= 0:
        return f"{c} is freezing temperature"
    else:
        return f"{c} is above freezing temperature"

def convert_to_celsius(temperature):
    return float((temperature - 32) * (5/9))