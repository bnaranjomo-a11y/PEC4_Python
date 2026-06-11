import unittest
import pandas as pd

from src.exercises.ex6 import fun_total_goals
class TestFunTotalGoals(unittest.TestCase):
   def test_fun_total_goals(self):
     data=pd.DataFrame({"FTHG":[2,1,3],"FTAG":[1,0,2]})
     resultado=fun_total_goals(data)
     self.assertEqual(resultado,/6,3,9))

if __name__=="__main__":
  unittest.main()
