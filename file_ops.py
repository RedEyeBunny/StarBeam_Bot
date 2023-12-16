import os
import time


# function to calculate age of file in days

def getfile_age(filepath) -> int:
    global day_age
    if os.path.exists(filepath):
        modification_time = os.path.getmtime(filepath)
        sec_age = time.time() - modification_time
        day_age = int(sec_age // (60 * 60 * 24))
    return day_age
