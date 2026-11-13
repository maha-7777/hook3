import unittest

# Application code
def add(a,b):
  return a+b

def subtract(a,b):
  return a-b
  
def multiply(a,b):
    return a*b

# Automated test cases 
class TestCalculator(unittest.TestCase):

  def test_add(self):
    self.assertEqual(add(10,20),40)

  def test_subtract(self):
    self.assertEqual(subtract(20,10),40)

  def test_multiply(self):
    self.assertEqual(multiply(6,4),24)

# amin application
if __name__=="__main__":
  print("student calculate application")
  print("addition:",add(20,20))
  print("subtraction:",subtract(20,10))
  print("multiplication:",multiply(5,4))

  print("\nExecting Automated Tests... \n")
  unittest.main(argv=['first-args-is-ignored'],exit=False)
