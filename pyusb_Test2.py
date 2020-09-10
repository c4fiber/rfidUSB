import usb.core
dev = usb.core.find(idVender=0x1d57, idProduct=0xac08)
if dev is None:
    raise ValueError('Device not Found')
dev.set_configuration()
