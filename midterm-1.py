# Author: IBN (AMDG)

import random
def clonemaker():
    total = []
    new_clone = random.randint(0, 9999)
    if new_clone < 1000 and new_clone > 99:
        return "New clone trooper name: CT-{0}{1}".format(0, new_clone)
    elif new_clone < 100 and new_clone > 9:
        return "New clone trooper name: CT-{0}{1}".format(00, new_clone)
    elif new_clone < 10 and new_clone > 0:
        return "New clone trooper name: CT-{0}{1}".format(000, new_clone)


clonemaker()


