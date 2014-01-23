from pyTestCase import PyTestCase
from pyException import PyException

class WasRun(PyTestCase):
    def __init__(self, name):
        PyTestCase.__init__(self, name)

    def setup(self):
        self.log = "setup"
    
    def testMethod(self):
        self.log += " testMethod"
        
    def tearDown(self):
        self.log += " tearDown"
        
    def testBrokenMethod(self):
        raise PyException

    
    
    
    
    
    



