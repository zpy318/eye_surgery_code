from pipython import GCSDevice, pitools

# Q motion controller setup
CONTROLLERNAME = 'E-873'

with GCSDevice(CONTROLLERNAME) as pidevice:
        pidevice.ConnectTCPIP(ipaddress='192.168.1.220')
        # pidevice.ConnectTCPIP(ipaddress='169.254.90.249')
        pitools.startup(pidevice, stages='Q-522.130', refmodes='FNL')
        # pidevice.MOV({'1': 1.2, '2': 3.7, '3': 0.7}) # eyerobot2.1 08/09/2022 '1': 1.2, '2': 3.7, '3': 0.7
        # pidevice.MOV({'1': 1.5, '2': 3.0, '3': 2.8}) # for TRO_2020 dataset, this zero position is '1': 1, '2': -2.5, '3': 0
        # pidevice.MOV({'1': 6.1, '2': 3.0, '3': -5}) # for eye reconstruction
        pidevice.MOV({'1': 0, '2': 0, '3': -5.5}) 
# CoRL
# '1': 2.1, '2': 1.1, '3': 2.5

# Randomization
# 1: +/- 0.5
# 2: +/- 0.5
# 3: +/- 0.5
