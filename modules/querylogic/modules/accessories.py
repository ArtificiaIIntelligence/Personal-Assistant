import json
import datetime
import os
import modules.access_util.timer as timer

def init_hook():
    access=Accessories()
    return access

class Accessories:
    def __init__(self):
        self.timers = [None] * 5
        self.timerNumbers = {0, 0, 0, 0, 0}

    def calculate_offset(alarmTime):
        return alarmTime-datetime.datetime.now()

    def stop_timer(self, numberOfTimer):
        self.timers(numberOfTimer).join()
        self.timers()

    def get_unassigned_number(self):
        for i in range(4):
            if self.timerNumbers(i) == 0:
                return i

        return -1

    def get_number_of_timer(value):
        #TODO: conversion of number
        return 1

    def call_timer(self, query):
        if 'set' in query['entities'] and 'time' in query['entities'] and len(self.timers)<6:
            if not (self.get_unassigned_number() == -1):
                timerNo = self.get_unassigned_number()
                alarmTime=int(query['entities']['time'][0]['value'])
                timeOffset=Accessories.calculate_offset(alarmTime)
                timerProcess=timer.run(timeOffset,timerNo,'wakeUpSong.mp3')
                self.timers.append(timerProcess)
                return 'Alarm set as timer number ' + str(len(self.timers))

        elif 'stop' in query['entities']:
            if len(self.timers)<1:
                return 'Currently, there are no running timers.'
            #elif not ('number' in query['entities']):
                #return 'Alarm number not specified, to stop all the alarms, please say: Stop all alarms'
            elif Accessories.get_number_of_timer(query['entities']['number'][0]['value']):
                numberOfTimer=Accessories.get_number_of_timer(query['entities']['number'][0]['value'])
                try:
                    self.stop_timer(self, numberOfTimer)
                    return 'Alarm number: ' + str(numberOfTimer) + ' has been stopped.'
                except:
                    return 'Unable to perform this command'
            else:
                return 'Unable to perform this command'

    def query_resolution(self, intent, query, params):
        if intent == 'timer':
            return self.call_timer(intent, query)
        else:
            return 'query not recognised'


