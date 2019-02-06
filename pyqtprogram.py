import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import pyqtSlot


from datetime import datetime
from escposprinter import *
from escposprinter.escpos import EscposIO, Escpos

class Printer():

    def __init__(self,ip,port):
        print("printer function")
        self.printerAddress= ip
        self.printerPort=port
        self.print_stuff()


    def checkPrinterAlive(self):
        if (printer.Network.isAlive(self.printerAddress, self.printerPort)):
            return True
        else:
            raise Exception ("Host is unreachable, socket communication was not opened")

    def print_stuff(self):
        if (self.checkPrinterAlive()):
                for iteration in range(1):
                    with EscposIO(printer.Network(self.printerAddress, self.printerPort)) as p:
                        p.set(font='a', codepage='cp1251', size='normal', align='center', bold=False)
                        #p.writelines('LOGO')
                        #p.printer.image('/Users/manick/alstom.png')
                        p.writelines('Sri City, Andhra Pradesh - India')
                        p.writelines('______________________________________')
                        p.set(font='a', codepage='cp1251', size='2x', align='center', bold=True)
                        p.writelines('')
                        p.writelines('BREAKFAST')
                        p.writelines('')
                        p.writelines('501')
                        p.writelines('')
                        p.set(font='a', codepage='cp1251', size='normal', align='center', bold=False)
                        now = datetime.now()
                        s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
                        p.writelines(s2)
                        p.writelines('')

class App(QWidget):
 
    def __init__(self,inp):
        super().__init__()
        self.title = 'Canteen Management System'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.seq=inp
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QPushButton('Click Me', self)
        button.setToolTip('This is an example button')
        button.move(100,70)
        print("Sequence:"+str(self.seq))
        button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        printerAddress = '192.168.2.6'
        printerPort = 9100
        for i in range(self.seq):
            print("printing:"+str(i))
            printer = Printer(printerAddress,printerPort)
            


if __name__ == '__main__':
    printerAddress = '192.168.2.6'
    printerPort = 9100
    inp=int(input("No of times to be print:"))
    app = QApplication(sys.argv)
    ex = App(inp)
    sys.exit(app.exec_())