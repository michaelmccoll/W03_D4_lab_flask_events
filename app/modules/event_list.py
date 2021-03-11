from app.modules.event import *
import datetime

event_1 = Event(datetime.date(2020, 6, 21), "Pub Crawl 2021", 100, 1, "world championship of pub crawling",False )
event_2 = Event(datetime.date(2020, 3, 13), "Cult BBQ", 20, 5, "sacrficial offering to our one true saviour", True )
event_3 = Event(datetime.date(2020, 4, 5), "Return to Codeclan", 50, 7, "triumphant return from remote life",False )
event_4 = Event(datetime.date(2020, 2, 29), "Free drinks festival", 200, 13, "The day it is my turn to pay for drinks",True )


events_list = [event_1, event_2, event_3, event_4]


def create_new_event(event):
    events_list.append(event)



