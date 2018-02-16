from cx_Freeze import setup, Executable
import sys
import os.path
base = None
if sys.platform == "win32":
    base = "Win32GUI"

#os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
#os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'
import os
includes = os.listdir("G:\\War_Time_Alarm\\build_alarm")
#print(includes)

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

setup(name = 'AlarmClock',
    version = "0.1",
    description = "Alarm Clock",
    options = {'build_exe':{'include_files':includes,'packages':['pygame','tkinter','pyowm','dill','PIL']}},
    executables=[Executable("Alarm_NEW.py", base= base)])