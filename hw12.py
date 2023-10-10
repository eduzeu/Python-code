'''
Eduardo Hernandez
I pledge my honor that I have abided by the Stevens Honor System.
December 2022
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
         as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        ''''Decides if self and d2 represent the same calendar date,
         whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        '''changes a date of the year to the following. For example, 01/01/2012 will
        return 01/02/2012
        DIM = (0,31,28,31,30,31,30,31,31,30,31,30,31)'''

        if self.month < 12:
            self.day +=1
            return 
            
        if self.month == 12:
            self.day = 1
            self.year += 1
            self.month = 1
            return 
            
        if self.isLeapYear() and self.month == 2 and self.day == 28:
            self.day += 1
            return

        if self.day == 31:
            self.month += 1
            return
        
        else:
             self.month = 1
             self.year += 1
        
