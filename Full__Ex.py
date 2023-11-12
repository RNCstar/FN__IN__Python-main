def printUsers(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}  value is: {value}")



printUsers(name="reza",family="babadi",age=23)
