import os

import psutil

import subprocess
def checkIfProcessRunning(processName):

    for proc in psutil.process_iter():
        try:

            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
if checkIfProcessRunning('Mullvad VPN.exe'):
    print('VPN is already running.')
else:
  path_to_mullvad = 'C:\\Program Files\\Mullvad VPN\\Mullvad VPN.exe'
  #path_to_daemon ='C:\\Program Files\\Mullvad VPN\\resources'
  subprocess.call([path_to_mullvad])
  print('VPN has been started!')

