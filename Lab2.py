import pickle
import os

class seat:
    def __init__(self,seatno,occupancy,lab):
        self.seatno = seatno
        self.lab = lab
        self.occupancy = occupancy

def main():
    #inner function/ encapsulation
    def makelab():
        with open("Lab2", 'wb') as f:
            for x in range(1,31):
                seatno = x
                lab = 1
                occupancy = 0
                s = seat(seatno, occupancy, lab)
                pickle.dump(s, f)
    #Inner function call
    makelab()




