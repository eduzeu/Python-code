'''
Eduardo Hernandez
I pledge my honor that I have abided by the Stevens Honor System.
9th December 2022
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
        '''changes a date of the year to the following day. For example, 01/01/2012 will
        return 01/02/2012'''
        DIM = (0,31,28,31,30,31,30,31,31,30,31,30,31)

        if self.day < DIM[self.month]:
            self.day +=1
            return 
        if self.month == 12 and self.day == 31:
            self.day = 1
            self.month = 1
            self.year += 1
            return 
        if self.month == 2 and self.isLeapYear() and self.day == 28:
            self.day += 1
            return
        else:
             self.month += 1
             self.day = 1

    def yesterday(self):
         '''Works opposite to yesterday. Instead of returning the day after, it returns
            the previous day of what it was entered. 1/1/2012 Will return
            12/31/2011'''
         DIM = (0,31,28,31,30,31,30,31,31,30,31,30,31)
         if self.day - 1 > 0:
             self.day -= 1
         else:
              if self.month == 1 and self.day == 1:
                 self.day = 31
                 self.month = 12
                 self.year -= 1
                 return
              if self.month == 3 and self.day == 1 and self.isLeapYear():
                 self.day = 29
                 self.month -=1
                 return
              else:
                 self.day = DIM[self.month-1]
                 self.month -= 1

    def addNDays(self, N):
         '''adds N amount of days to the date entered. If N = 4 it will add four days.
            i.e We have 1/1/13 the output will be 1/4/13'''
         if N > 0:
             for date in range(N):
                 print(self)
                 self.tomorrow()
             print(self) 
             
    def subNDays(self, N):
        '''Subtracts N amount of days to the date entered. If N = 4 it will subtract
            four days. i.e We have 1/4/13 the output will be 1/1/13'''
        if N > 0:
            for date in range(N):
                print(self)
                self.yesterday()
            print(self)

    def isBefore(self, d2):
        '''gets a date d2 and checks whether the date entered is before a date d.
            if the date is before returns true, if it's equal or after it will
            return false'''
        if self.year == d2.year and self.month == d2.month and \
           self.day == d2.day:
            return False
        else:
            if self.year < d2.year:
                return True
            if self.year == d2.year and self.month < d2.month:
                return True
            if self.day < d2.day and self.month == d2.month:
                return True
            if self.month < d2.month and self.year <= d2.year:
                return True 

    def isAfter(self, d2):
        '''reveres the process of isBefore. If the the date entered is after it will
            return True, otherwise it will return False.'''
        if self.year == d2.year and self.month == d2.month and \
           self.day == d2.day:
            return False
        else:
            if self.year > d2.year:
                return True
            if self.year == d2.year and self.month > d2.month:
                return True
            if self.day > d2.day and self.month == d2.month:
                return True
            if self.month > d2.month and self.year >= d2.year:
                return True  

    def diff(self, d2):
        '''Returns an integer representing the distance between the dates entered.
           If the date entered is the same, it will return zero, if it's before the
           previous date, it will return the distance in negative'''
        if self.equals(d2):
            return 0
        dayCounter = 0 
        firstDate = self.copy()
        secondDate = d2.copy()
        while firstDate.equals(secondDate) == False: #dates are not equal to each other
            if firstDate.isAfter(secondDate):
                firstDate.yesterday()
                dayCounter += 1
            else:
                secondDate.yesterday()
                dayCounter -= 1
        return dayCounter
    
    def dow(self):
        '''returns a day of the week based on the date entered. i.e It takes july 6th
            2009, which started on Monday and therefore the List begins on Monday '''
        
        dowList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return dowList[self.diff(Date(7, 6, 2009)) % 7]
