
import usb.core
import usb.util

# find our device
dev = usb.core.find(idVendor=0x1D57, idProduct=0xAC08)

# was it found?
if dev is None:
    raise ValueError('Device not found')

print(dev)

'''
#read
cnt = 0
attempts = 2
while cnt < attempts:
    try:
        #read(wEndpointAddress, wMaxPcketSize) from USB Description
        data = dev.read(0x81, 8)
        cnt += 1
        print(data)
    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out'):
            continue

'''
'''
# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('test')

dev.reset()
'''
