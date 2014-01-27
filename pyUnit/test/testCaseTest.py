'''
Created on 2013-12-28

@author: it
'''
from pyTestCase import PyTestCase
from wasRun import WasRun
from pyTestResult import PyTestResult
import pyTestSuite
from pyTestSuite import PyTestSuite

class TestCaseTest(PyTestCase):
    def testTemplateMethod(self):
        print 'testTemplateMethod'
        test = WasRun("testMethod")
        result = PyTestResult()
        test.run(result)
        assert "setup testMethod tearDown" == test.log, ('Expected:1 run, 0 failed, Current:' + result.summary())
        
    def testResult(self): 
        print 'testResult'
        test = WasRun('testMethod')
        result = PyTestResult()
        test.run(result)
        assert "1 run, 0 failed" == result.summary(), ('Expected:1 run, 0 failed, Current:' + result.summary())
        
    def testBrokenMethod(self):
        print 'testBrokenMethod'
        test = WasRun('testBrokenMethod')
        result = PyTestResult()
        test.run(result)
        assert "1 run, 1 failed" == result.summary(), ('Expected:1 run, 0 failed, Current:' + result.summary())
        
    def testFailedResultFormatting(self):
        print 'testFailedResultFormatting'
        result = PyTestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == result.summary(), ('Expected:2 run, 1 failed, Current:' + result.summary())
        
    def testTestSuite(self):
        suite = pyTestSuite()
        suite.add(WasRun('testMethod'))
        suite.add(WasRun('testBrokenMethod'))
        
        result = PyTestResult()
        suite.run(result)
        assert "2 run, 1 failed" == result.summary(), ('Expected:2 run, 1 failed, Current:' + result.summary())
        
'''
print '------------------------begin test------------------------'
print TestCaseTest("testTemplateMethod").run().summary()
print TestCaseTest("testResult").run().summary()
print TestCaseTest("testFailedResultFormatting").run().summary()
print TestCaseTest("testBrokenMethod").run().summary()
print '-------------------------end test-------------------------'
'''
suite = PyTestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testBrokenMethod"))
result = PyTestResult()
suite.run(result)
print result.summary()