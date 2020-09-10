import hid

hid.initialise()
d = pyhid.scan_devices()

print(d.name)
print(d)

vID = 0x1d57
pId = 0xac08


pyhid.finalise()