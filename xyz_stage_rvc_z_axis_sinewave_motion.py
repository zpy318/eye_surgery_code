from pipython import GCSDevice, pitools
import time
import random
import numpy as np

# Q motion controller setup
CONTROLLERNAME = 'E-873'

with GCSDevice(CONTROLLERNAME) as pidevice:
    pidevice.ConnectTCPIP(ipaddress='192.168.1.220')
    pitools.startup(pidevice, stages='Q-522.130', refmodes='FNL')
    # step = 18 * 21.8049 / 1000
    # dy = 1.00386734 * step
    # dz = 0.55403648 * step
    dy = 0
    dz = 0
    xaxis = '1'
    yaxis = '2'
    zaxis = '3'
    xvalue = 0
    yvalue = 0
    pidevice.CCL('1', 'ADVANCED')
    pidevice.SPA('1', '0x1F000400', 25000) # Hz range 150Hz - 25000Hz
    pidevice.SPA('2', '0x1F000400', 25000) # Hz range 150Hz - 25000Hz
    pidevice.SPA('3', '0x1F000400', 10000) # Hz range 150Hz - 25000Hz
    pidevice.MOV({'1': 0, '2': 0, '3': -5.5})
    count = 1
    while (True):
        # xvalue = np.random.rand() * 4 - 1
        # yvalue = np.random.rand() * 4 - 1
        zvalue = -5.5 + 0.1 * np.sin(np.pi * count * 0.015)
        # pidevice.MOV(axis, value) # for TRO_2020 dataset, this zero position is '1': 1, '2': -2.5, '3': 0
        pidevice.MOV({'1': xvalue, '2': yvalue, '3': zvalue})
        # while(pidevice.IsMoving(zaxis)['3']):
        #     print("It is moving along z-aixs with sinewave pattern.")
        count += 1
        # time.sleep(0.03)
        # # print(pidevice.IsMoving(axis)['1'])
        # pidevice.MOV(axis, -value)
        # while(pidevice.IsMoving(axis)['1']):
        #     print()

# 5, 2, 5.5 (zero)
# 0.9, 0.6, 2.8 (CDC_old)
# 1.2, 2.2, 2.8 (CDC_new)
# 1.1, 2.7, 2.8 (CDC_newest)

# CoRL
# '1': -1.35, '2': -0.5, '3': 0

# Randomization
# 1: +/- 0.5
# 2: +/- 0.5
# 3: +/- 0.5
