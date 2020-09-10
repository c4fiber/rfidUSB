import pywinusb.hid as hid

idVender = 0x1d57
idProduct = 0xac08

def readData(data):
    print("Raw Data: {0}".format(data))
    return None

filter = hid.HidDeviceFilter(vendor_id = idVender, product_id = idProduct)
hid_devices = filter.get_devices()
print(hid_devices)



'''
device = hid_devices[0]

device.open()
print(hid_devices)

target_usage = hid.get_full_usage_id(0x00, 0x3f)
device.set_raw_data_handler(readData)
print(target_usage)

report = device.find_output_reports()

print(report)
print(report[0])

buffer = [0xFF]*64
buffer[0] = 63

print(buffer)

report[0].set_raw_data(buffer)
report[0].send()
'''