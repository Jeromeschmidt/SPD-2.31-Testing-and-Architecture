# by Kami Bigdely
# Docstrings and blank lines


class OnBoardTemperatureSensor:
    """Class for On-Board Temperature Sensor"""

    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        """init function"""
        pass

    def read_voltage(self):
        """read voltage"""
        return 2.7

    def get_temperature(self):
        """get temperature"""
        # [celcius]
        return self.read_voltage() * \
        OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR


class CarbonMonoxideSensor:
    """Class for Carbon Monoxide Sensor"""

    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        """init function"""
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """get carbon monoxide level"""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor. \
        convert_voltage_to_carbon_monoxide_level(sensor_voltage,
                                                 self.on_board_temp_sensor.
                                                 get_temperature())
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """get sensor voltage"""
        # In real life, it should read from hardware.
        return 2.3

    def convert_voltage_to_carbon_monoxide_level(voltage, temperature):
        """convert voltage to carbon monoxide level"""
        return voltage * \
        CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature


class DisplayUnit:
    """Class for Display Unit Sensor"""

    def __init__(self):
        """init function"""
        self.string = ''

    def display(self, msg):
        """display message"""
        print(msg)


class CarbonMonoxideDevice():
    """Class for Carbon Monoxide Device Sensor"""

    def __init__(self, co_sensor, display_unit):
        """init function"""
        self.carbonMonoxideSensor = co_sensor
        self.display_unit = display_unit

    def Display(self):
        """send message to display to display function"""
        msg = 'Carbon Monoxide Level is : ' + \
        str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)


if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()
