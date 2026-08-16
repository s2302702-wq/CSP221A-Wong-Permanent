from functools import wraps
import logging
from abc import ABC, abstractmethod
logging.basicConfig(level=logging.INFO)


class InsufficientBatteryError(Exception):
    def __init__(self, robot_name, required, available):
        self.robot_name = robot_name
        self.required = required
        self.available = available

        super().__init__(
            f"{robot_name} needs {required}% battery for this task "
            f"but only has {available}%."
        )
class Robot(ABC):
    manufacturer = "RoboTech"
    population = 0

    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery
        Robot.population += 1

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        if value < 0:
            self._battery = 0
        elif value > 100:
            self._battery = 100
        else:
            self._battery = value

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', battery={self.battery})"

    def use_battery(self, amount):
        if self.battery < amount:
            raise InsufficientBatteryError(
                self.name, amount, self.battery
            )
        self.battery -= amount

    @classmethod
    def from_config(cls, config):
        return cls(
            config["name"],
            config.get("battery", 100)
        )

    @abstractmethod
    def perform_task(self):
        pass
def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished {func.__name__}")
        return result
    return wrapper

class CleaningRobot(Robot):
    def __init__(self, name, battery=100, dust_capacity=10):
        super().__init__(name, battery)
        self.dust_capacity = dust_capacity
    @log_action
    def perform_task(self):
     self.use_battery(20)
     return "Cleaning the floor"

class DroneRobot(Robot):
    def __init__(self, name, battery=100, max_altitude=100):
        super().__init__(name, battery)
        self.max_altitude = max_altitude
    def perform_task(self):
     self.use_battery(10)
     return "Flying and surveying"

def fleet_report(robots):
    for robot in robots:
        print(str(robot))
def run_task_safely(robot, **kwargs):
    try:
        result = robot.perform_task(**kwargs)
    except InsufficientBatteryError as error:
        logging.error(error)
    else:
        print(result)
    finally:
        print(f"{robot.name} current battery: {robot.battery}%")

class BadRobot:
    tasks = []

class GoodRobot:
    def __init__(self):
        self.tasks = []
bad1 = BadRobot()
bad2 = BadRobot()

bad1.tasks.append("Clean")

print(bad1.tasks)
print(bad2.tasks)

good1 = GoodRobot()
good2 = GoodRobot()

good1.tasks.append("Clean")

print(good1.tasks)
print(good2.tasks)
