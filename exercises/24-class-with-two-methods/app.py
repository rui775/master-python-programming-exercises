class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())

def test_class():
    strObj = InputOutString()
    strObj.getString()
    strObj.printString()

# Test the class
test_class()
