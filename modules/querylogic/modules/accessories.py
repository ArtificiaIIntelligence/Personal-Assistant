import json
import datetime
import os
import modules.access_util.timer as timer

def init_hook():
    access=Accessories()
    return access

class Accessories:
    def __init__(self):
        self.timers = {0:0,1:0,2:0,3:0,4:0}

    def calculate_offset(alarmTime):
        time = alarmTime[:-6]  # Ignore timezone
        timeZone = alarmTime[-6:-3]
        utc = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.000')
        utc = utc + datetime.timedelta(hours=int(timeZone))
        return utc-datetime.datetime.now()

    def stop_timer(self, numberOfTimer):
        self.timers[numberOfTimer].join()

    def get_unassigned_number(self):
        for key,p in self.timers.values():
            try:
                if not p.is_alive():
                    self.timers[key]=None
            except:
                self.timers[key] = None

            if self.timers[key]==None:
                return key

        return -1

    def get_number_of_timer(value):
        #TODO: conversion of number
        return 1

    def call_timer(self, query):
        #TODO: get timer alarm time
        if 'set' in query['entities'] and 'time' in query['entities']:
            if self.get_unassigned_number() != -1:
                timerNo = self.get_unassigned_number()
                alarmTime=int(query['entities']['time'][0]['value'])
                timeOffset=Accessories.calculate_offset(alarmTime)
                timerProcess=timer.run(timeOffset,timerNo,'wakeUpSong.mp3')
                self.timers[timerNo] = timerProcess
                return 'Alarm set as timer number ' + str(timerNo) + '.'
            else:
                'The capacity of the timers is filled.'

        elif 'stop' in query['entities']:
            #TODO: stop all alarms
            if Accessories.get_number_of_timer(query['entities']['number'][0]['value']):
                numberOfTimer = Accessories.get_number_of_timer(query['entities']['number'][0]['value'])
                try:
                    self.stop_timer(self, numberOfTimer)
                    return 'Alarm number: ' + str(numberOfTimer) + ' has been stopped.'
                except:
                    return 'Unable to perform this command, are you sure that this timer is running?.'
            else:
                return 'The number specified is not valid.'
        else:
            return 'I am sorry, I am not sure what you meant.'

    def query_resolution(self, intent, query, params):
        if intent == 'timer':
            return self.call_timer(query)
        else:
            return 'query not recognised'


