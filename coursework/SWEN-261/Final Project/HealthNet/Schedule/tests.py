import datetime
from django.http import Http404

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Appointment
from .views import getNextDay, getPrevDay, getNextDayUrl, getPrevDayUrl, getNextWeekUrl, getPrevWeekUrl, getNextYearUrl, getPrevYearUrl

def createAppointment1():
    app = Appointment
    app.startTime = ['2015-10-1 12:12:12']
    app.endTime = ['2017-10-1 12:12:12']
    app.description = "desc"
    app.comments = "comments"

def createAppointment2():
    app = Appointment
    app.startTime = ['2015-10-1 12:12:12']
    app.endTime = ['2015-12-1 12:12:12']
    app.description = "desc"
    app.comments = "comments"

def createAppointment3():
    app = Appointment
    app.startTime = ['2015-10-1 12:12:12']
    app.endTime = ['2015-10-9 12:12:12']
    app.description = "desc"
    app.comments = "comments"

def createAppointment4():
    """
    case where endtime exists before start time
    test the try-catch error
    :return:
    """
    app = Appointment
    app.startTime = ['2015-10-1 12:12:12']
    app.endTime = ['1111-1-11 11:11:11']
    app.description = "desc"
    app.comments = "comments"

class AppointmentTestCase(TestCase):

    def errorChecking(self):
        """
        test case for error
        :return: if error exist, then the function will skip without crashing the program
        """
        try:
            a = createAppointment4()
        except Http404("User does not exist"):
            pass

class ViewsTestCase(TestCase):
    def testIndex(self):
        resp = self.client.get('/Schedule/')
        self.assertEqual(resp.status_code, 200)

    def testGetNextYearUrl(self):
        year1 = '1/1/1/'
        year2 = '3/3/3/'
        self.assertEqual(getNextYearUrl(1,1,0), year1)
        self.assertEqual(getNextYearUrl(3,3,2), year2)

    def testGetPrevYearUrl(self):
        year1 = '1/1/1/'
        year2 = '3/3/3/'
        self.assertEqual(getPrevYearUrl(1,1,2), year1)
        self.assertEqual(getPrevYearUrl(3,3,4), year2)

    def testGetPrevDayUrl(self):
        dayDec = '12/12/12/'
        dayDec2 = '12/12/31/'
        dayNov = '11/11/11/'
        dayNov2 = '11/11/30/'
        dayFebLeapYear = '12/2/29/'
        dayFeb2 = '11/2/28/'
        self.assertEqual(getPrevDayUrl(12, 13, 12), dayDec)
        self.assertEqual(getPrevDayUrl(1, 1, 13), dayDec2)
        self.assertEqual(getPrevDayUrl(11, 12, 11), dayNov)
        self.assertEqual(getPrevDayUrl(12, 1, 11), dayNov2)
        self.assertEqual(getPrevDayUrl(3, 1, 12), dayFebLeapYear)
        self.assertEqual(getPrevDayUrl(3, 1, 11), dayFeb2)

    def testGetNextDayUrl(self):
        dayDec = '12/12/12/'
        dayDec2 = '13/1/1/'
        dayNov = '11/11/11/'
        dayNov2 = '11/12/1/'
        dayFebLeapYear = '12/2/29/'
        dayFeb2 = '11/3/1/'
        self.assertEqual(getNextDayUrl(12, 11, 12), dayDec)
        self.assertEqual(getNextDayUrl(12, 31, 12), dayDec2)
        self.assertEqual(getNextDayUrl(11, 10, 11), dayNov)
        self.assertEqual(getNextDayUrl(11, 30, 11), dayNov2)
        self.assertEqual(getNextDayUrl(2, 28, 12), dayFebLeapYear)
        self.assertEqual(getNextDayUrl(2, 28, 11), dayFeb2)

    def testGetPrevDay(self):
        dayDec = ('12','12','12')
        dayDec2 = ('12','31','12')
        dayNov = ('11','11','11')
        dayNov2 = ('11', '30', '11')
        dayFebLeapYear = ('2', '29', '12')
        dayFeb2 = ('2', '28', '11')
        self.assertEqual(getPrevDay(12, 13, 12), dayDec)
        self.assertEqual(getPrevDay(1, 1, 13), dayDec2)
        self.assertEqual(getPrevDay(11, 12, 11), dayNov)
        self.assertEqual(getPrevDay(12, 1, 11), dayNov2)
        self.assertEqual(getPrevDay(3, 1, 12), dayFebLeapYear)
        self.assertEqual(getPrevDay(3, 1, 11), dayFeb2)

    def testGetPrevWeekUrl(self):
        weekDec = '12/12/12/'
        weekDec2 = '12/12/31/'
        weekNov = '11/11/11/'
        weekNov2 = '11/11/30/'
        weekFebLeapYear = '12/2/29/'
        weekFeb2 = '11/2/28/'
        self.assertEqual(getPrevWeekUrl(12, 19, 12), weekDec)
        self.assertEqual(getPrevWeekUrl(1, 7, 13), weekDec2)
        self.assertEqual(getPrevWeekUrl(11, 18, 11), weekNov)
        self.assertEqual(getPrevWeekUrl(12, 7, 11), weekNov2)
        self.assertEqual(getPrevWeekUrl(3, 7, 12), weekFebLeapYear)
        self.assertEqual(getPrevWeekUrl(3, 7, 11), weekFeb2)

    def testGetNextDay(self):
        dayDec = ('12', '12', '12')
        dayDec2 = ('1', '1', '13')
        dayNov = ('11', '11', '11')
        dayNov2 = ('12', '1', '11')
        dayFebLeapYear = ('2', '29', '12')
        dayFeb2 = ('3', '1', '11')
        self.assertEqual(getNextDay(12, 11, 12), dayDec)
        self.assertEqual(getNextDay(12, 31, 12), dayDec2)
        self.assertEqual(getNextDay(11, 10, 11), dayNov)
        self.assertEqual(getNextDay(11, 30, 11), dayNov2)
        self.assertEqual(getNextDay(2, 28, 12), dayFebLeapYear)
        self.assertEqual(getNextDay(2, 28, 11), dayFeb2)

    def testGetNextWeekUrl(self):
        weekDec = '12/12/12/'
        weekDec2 = '13/1/7/'
        weekNov = '11/11/11/'
        weekNov2 = '11/12/7/'
        weekFebLeapYear = '12/3/6/'
        weekFeb2 = '11/3/7/'
        self.assertEqual(getNextWeekUrl(12, 5, 12), weekDec)
        self.assertEqual(getNextWeekUrl(12, 31, 12), weekDec2)
        self.assertEqual(getNextWeekUrl(11, 4, 11), weekNov)
        self.assertEqual(getNextWeekUrl(11, 30, 11), weekNov2)
        self.assertEqual(getNextWeekUrl(2, 28, 12), weekFebLeapYear)
        self.assertEqual(getNextWeekUrl(2, 28, 11), weekFeb2)