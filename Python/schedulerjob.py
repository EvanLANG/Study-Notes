#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 17:27:32 2018

@author: evan
"""

"""
Demonstrates how to use the blocking scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    print('Press Ctrl+C to exit')

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
        
        
        
        
#from datetime import datetime
#import os
#
#from twisted.internet import reactor
#from apscheduler.schedulers.twisted import TwistedScheduler
#
#
#def tick():
#    print('Tick! The time is: %s' % datetime.now())
#
#
#if __name__ == '__main__':
#    scheduler = TwistedScheduler()
#    scheduler.add_job(tick, 'interval', seconds=3)
#    scheduler.start()
#    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
#
#     #Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
#    try:
#        reactor.run()
#    except (KeyboardInterrupt, SystemExit):
#        pass
##    while True:
##        print("This is the main thread.")
##        time.sleep(2)