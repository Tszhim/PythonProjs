import time
import math


class TimeChecker:

    # Storing starting time.
    def __init__(self):
        self.start = time.time()

    # Checking if allotted time is over.
    def times_up(self):
        return time.time() - self.start >= 600

    # Returns minutes left.
    def curr_min(self):
        return math.floor(10 - (time.time() - self.start) / 60)

    # Returns seconds left.
    def curr_sec(self):
        return round(60 - (time.time() - self.start) % 60)
