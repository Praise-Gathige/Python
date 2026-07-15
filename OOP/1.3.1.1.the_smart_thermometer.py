class Thermometer:
    def __init__(self):
        self.__celsius = 0

    @property
    def temperature(self):
        return self.__celsius

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            print("Error: The temperature cannot drop below -273.15!")
            self.__celsius = 0
        else:
            self.__celsius = value


# Running the program
my_therm = Thermometer()
my_therm.temperature = -300