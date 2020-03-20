import socket
import sys
import os


path = os.getcwd()
print(path)
name = os.path.basename(sys.argv[0]).rstrip('.py')
sys.path.append(path)
print(name)
rms1 = __import__(name)
dir(rms1)

class rm_define():
    def __init__(self):
        self.robot_mode_gimbal_follow = 1
        self.robot_mode_chassis_follow = 2
        self.robot_mode_free = 3
        self.timer_start = 1
        self.timer_stop = 2
        self.timer_reset = 3
class robot():
    def __init__(self):
        pass
    def set_mode(self,mode_enum):
        self.mode = mode_enum

class tools(robot):
    def __init__(self):
        pass
    def timer_ctrl(self,behavior_enum):
        self.behavior_enum = behavior_enum
    def timer_current(self):
        pass
    def run_time_of_program(self):
        pass

class FunctionError(Exception):
    "this is user's Exception for check the length of name "
    def __init__(self,leng):
        pass

try:
    rms1.start()
except AttributeError:
    raise TypeError('no start function')
