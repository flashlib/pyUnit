'''
@author: it
'''

class PyTestSuite(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.tests = []
        
    def add(self, test):
        self.tests.append(test)
        
    def run(self, result):
        for test in self.tests:
            test.run(result)
        