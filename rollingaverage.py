#import math

"""
Class Name: Rolling_Average
Class Description:
    1. provides rolling average functionality
    which can be adjusted by using a
    deviator to adjust weights
    2. also has a midrange formula which
    is updated alongside the rolling average
    3. does not maintain a list of values
    added, aside from current and previous,
    but instead updates a formula
    4. as a result it is not slowed by extended running.
    5. has no dependencies other than the standard python library
Class Methods:
    setdeviator - sets the deviator to adjust weighting (not currently used)
    update - the main function of the class, which updates the values calculated by the formulae
    rollingformula - used to calculate the rolling average
    getrolling -  used to return the calculated value of rolling
NOTE:
    until update is called, getrolling & getmidrange return the value 0
PENDING:
    future update will clarify how deviator works to produce an emulated exponential moving average
    may need review to ensure that current formula is used in this file
"""    
class Rolling_Average:
    def __init__(self):
        self.n = 0
        self.count =0
        self.rolling = 0
        self.maxn = 0
        self.minn = 999999999
        self.divisor = 2
        self.midrange = 0
        self.deviator = 0
        self.currentn = 0
        self.previousn = 0
        self.weight1 = 1
        self.weight2 = 1
    def setdeviator(self, d = 0):
        """
        NOTE:
        deviate to current with positive deviator
        deviate to past using negative deviator
        deviator should be of value .99 to -.99
        """
        self.deviator = d
        self.weight1 = self.weight1 - self.deviator
        self.weight2 = self.weight2 + self.deviator
    def update(self, n):
        self.previousn = self.n
        self.n = n
        self.currentn = self.n
        self.count = self.count + 1
        self.updatemin(n)
        self.updatemax(n)
        self.weight1 = 1
        self.weight2 = 1
        self.rollingformula()
        self.midrangeformula()
    def updatemin(self, n):
        if(n < self.minn):
            self.minn = n
    def updatemax(self, n):
        if(n > self.maxn):
            self.maxn = n
    def rollingformula(self):
        """
        Approximation of a rolling average, but with no simple average.
        """
        if(self.count > 1):
            self.rolling = ((self.rolling * (self.count - 1)) + self.currentn))/self.count
        else:
            self.rolling = self.currentn
    def midrangeformula(self):
        if(self.count > 0):
            self.midrange = (self.minn + self.maxn)/2
    def getcurrent(self):
        return self.currentn
    def getrolling(self):
        return self.rolling
    def getmidrange(self):
        return self.midrange
    def getcount(self):
        return self.count
    def getstring(self):
        stringvalue = "the estimate of rolling average is: " + str(self.rolling) + ". \n" + \
                      "Current midrange value is: " + str(self.midrange)
        return stringvalue

        
"""
#as a library this isn't needed, but it may be needed for testing purposes.
def main():
    ra = Rolling_Average()
    uval = 0
    while(uval >= 0):
        print(ra.getstring())
        try:
            uval = int(input("Enter an integer/whole number, or enter negative number to exit: "))
        except ValueError:
            print("Invalid input, enter only whole numbers")
        ra.update(uval)
        #print(uval)
        #print(ra.getcurrent())
"""
        

"""
if __name__ == "__main__":
    main()
    exit()
"""
