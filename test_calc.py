
import unittest
import calfolder.calc  

# calc is the file to be tested
# test_calc is to run the test

class TestCalc(unittest.TestCase):
     # below method name  must be start with test
     def test_add(self):
         self.assertEqual(calc.add(10,5),15)
         self.assertEqual(calc.add(-1,1),0)
         self.assertEqual(calc.add(-1,-1),-2)

if __name__ =='__main__':
    unittest.main()


# python3 -m unittest test_calc.py 
# after adding the above if clause.
# run command at CLI 
# python3 test_calc.py 
