import DIC
import os

if __name__ == '__main__':
    dci = DIC.DIC(r"/home/lepitopperson/Desktop/test.csv")
    dci.calculate()
    print(dci.result)
