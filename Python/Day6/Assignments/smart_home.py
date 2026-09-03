class SmartThermostat:
    min_temp = 10.0
    max_temp = 35.0

    def __init__(self, appliance_name: str, initial_temp: float):
        self.__appliance_name = appliance_name
        if self.min_temp <= initial_temp <= self.max_temp:
            self.__target_temp = initial_temp
        else:
            self.__target_temp = 22.0

    @property
    def target_temp(self) -> float:
        return self.__target_temp

    @target_temp.setter
    def target_temp(self, value: float):
        if self.min_temp <= value <= self.max_temp:
            self.__target_temp = value
        else:
            raise ValueError("Temperature must be between 10.0 and 35.0 degrees.")

    @property
    def appliance_name(self) -> str:
        return self.__appliance_name

thermostat = SmartThermostat("Living Room AC", 24.0)
print(thermostat.appliance_name)  # Output: Living Room AC
print(thermostat.target_temp)     # Output: 24.0

thermostat.target_temp = 28.0     # Updates successfully
print(thermostat.target_temp)     # Output: 28.0

try:
    thermostat.target_temp = 5.0  # Out of range!
except ValueError as e:
    print(e)  # Output: Temperature must be between 10.0 and 35.0 degrees.