import os

from item import Item


def getMacList():
    results = os.popen('arp-scan -l').readlines()
    l = len(results)
    m = {}
    for i in range(2, l - 3):
        temp = results[i].split('\t')
        if len(temp) < 3:
            continue
        item = Item()
        item.desc = temp[2].strip()
        item.ip = temp[0].strip()
        item.mac = temp[1].strip()
        m[item.mac] = item
    return m


m = getMacList()
print(m)
