import usb.core
import usb.util

dev = usb.core.find(idVendor=0x1d57, idProduct=0xac08)

if dev is None:
    raise ValueError('Device not found')

raw_input("")

reqType = ''
bReq = ''
wVal = ''
wIndex = ''

dev.ctrl_transfer(reqType, bReq, wVal, wIndex, [])
