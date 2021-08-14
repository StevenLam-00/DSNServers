def formatheader():
    print(
        "Country |    Count     |\n"
        "--------+-------------+|")


def sortbycode():
    device_file = open('DNSList.txt', 'r')
    formatheader()
    devices = []
    for line in device_file:
        devices.append([i for i in line.strip("\n").split("of")])
    devices.sort(key=lambda x: x[0])
    for device in devices:
        print("{0:5} | {1:13}".format(*device))
sortbycode()