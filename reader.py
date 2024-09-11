import time

from pn532pi import Pn532, pn532
from pn532pi import Pn532I2c
from pn532pi import Pn532Spi
from pn532pi import Pn532Hsu

# Set the desired interface to True
SPI = False
I2C = True
HSU = False

if SPI:
    PN532_SPI = Pn532Spi(Pn532Spi.SS0_GPIO8)
    nfc = Pn532(PN532_SPI)
elif HSU:
    PN532_HSU = Pn532Hsu(0)
    nfc = Pn532(PN532_HSU)

elif I2C:
    PN532_I2C = Pn532I2c(1)
    nfc = Pn532(PN532_I2C)

password =  bytearray([ 0x12, 0x34, 0x56, 0x78])

def setup():
    nfc.begin()
    versiondata = nfc.getFirmwareVersion()

    if not versiondata:
        print("Didn't find PN53x board")
        raise RuntimeError("Didn't find PN53x board")
    
    nfc.SAMConfig()

def listen():
    setup()
    while True:
        print('Waiting for tag...')
        tag_present = False

        while not tag_present:
            time.sleep(.1)
            tag_present, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)

        print('Tag found!')
        decoded_uid = ''

        tag_present, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)
        
        for i in uid:
            decoded_uid += str(int(i))

        print('UID:', decoded_uid)
        return decoded_uid
    
def listen_non_blocking():
    setup()
    #print('Waiting for tag...')
    tag_present = False
    tag_present, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)

    if tag_present:
        print('Tag found!')
        decoded_uid = ''
        
        for i in uid:
            decoded_uid += str(int(i))

        print('UID:', decoded_uid)
        return decoded_uid
    else:
        return 0
