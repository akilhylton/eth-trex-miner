import os
import platform
import subprocess

OS = platform.system()

if OS == 'Linux':
    process = subprocess.call('scripts/run_miner')
    
elif OS == 'Darwin':
    print('Error: Mac OS is not supported, please use Windows or Linux.')
