'''
Created on 4/5/2015

@author: Daniela Ortiz (10-10517)
         Maria Lourdes Garcia (10-10264)
'''
import unittest
from BilleteraElectronica import *

class TestBilleteraElectronica(unittest.TestCase):
    
    # Caso para verificar que existe la clase Billetera Electronica
    
    def TestBilleteraElectronicaExist(self):
        BilleteraElectronica("AfJ556tY", "Nelson", "Gonzalez", 19994187, 123456)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()