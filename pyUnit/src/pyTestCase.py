from pyTestResult import PyTestResult

class PyTestCase(object):
    def __init__(self, name):
        self.name = name
        
    def setup(self):
        pass
    
    def tearDown(self):
        pass
    
    def run(self):
        result = PyTestResult()
        result.testStarted()        
        self.setup()
        
        #if catch exception here, the assert statement will not work in TestCaseTest
        try:
            method = getattr(self, self.name)
            method()
        except AssertionError, e:
            print e
            raise
        except Exception, e:
            result.testFailed()
         
        self.tearDown()
        return result


