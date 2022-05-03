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
    setdeviator - sets the deviator to adjust weighting
    update - the main function of the class, which updates the values calculated by the formulae
    rollingformula - used to calculate the rolling average
    getrolling -  used to return the calculated value of rolling
NOTE:
    until update is called, getrolling & getmidrange return the value 0
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
        self.weight1 = 1 - self.deviator
        self.weight2 = 1 + self.deviator
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
            self.rolling = (self.rolling/(self.divisor))*self.weight1 + (self.currentn/(self.divisor))*self.weight2
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
Original Procedural Program... was converted to class. 
    n = 0
    count = 0
    rolling = 0
    maxn = 0
    minn = 0
    divisor = 2
    midrange = 0
    
    deviate to current with positive deviator
    deviate to past using negative deviator
    deviator should be of value .99 to -.99
    
    deviator = .37
    while(n >= 0):
        if (count > 0):
            print("the rolling estimate of average is: " + str(rolling))
            print("midrange is: " + str(midrange))
        count = count + 1
        previousn = n
        
        n =  int(input("enter an integer/whole number, or negative number to exit: "))
        currentn = n
        if(currentn > maxn):
            maxn = currentn
        if (currentn < minn):
            minn = currentn
        if (count > 1):
            weight1 = 1 - deviator
            weight2 = 1 + deviator
            rolling = (rolling/(divisor))*weight1 + (currentn/(divisor))*weight2
            
        else:
            rolling = currentn
            minn = currentn
        midrange = (maxn+minn)/2
      """  
"""
if __name__ == "__main__":
    main()
    exit()
"""
