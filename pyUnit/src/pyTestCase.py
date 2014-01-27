from pyTestResult import PyTestResult
from pyException import PyException

class PyTestCase(object):
    def __init__(self, name):
        self.name = name
        
    def setup(self):
        pass
    
    def tearDown(self):
        pass
    
    def run(self, result):
        result.testStarted()        
        self.setup()
        
        #if catch exception here, the assert statement will not work in TestCaseTest
        try:
            method = getattr(self, self.name)
            method()
        except PyException:
            result.testFailed()            
        #except AssertionError, e:
        #    print e
        #    raise
         
        self.tearDown()


