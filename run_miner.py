import os
import platform

OS = platform.system()

if OS == 'Linux':
    POOL=input("Enter pool location: ")
    WALLET=input("Enter wallet address: ")
    process = subprocess.run(['sh', 'scripts/run_miner', POOL, WALLET],
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
elif OS == 'Darwin':
    print('Error: Mac OS is not supported, please use Windows or Linux.')
