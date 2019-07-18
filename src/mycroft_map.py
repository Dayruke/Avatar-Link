#!/usr/bin/env python

# WS client example
'''
Mycroft Map
Receives messages as they appear on Mycroft's Message Bus and
Returns Message for use on the Avatar Channel
'''

import re

class MycroftMap:

    def __init__(self):
        pass

    # app channel msg --> avatar channel msg
    def translate(self, msg):

        if (re.match('.*enclosure.reset',msg)):
            translatedMessage = 'reset'

        # test broadcast with *reminder* : a regular app channel message
        elif (re.match('.*mycroft-reminder',msg)):
            translatedMessage = 'reminder_Test'

        elif (re.match('.*enclosure.mouth.talk',msg)):
            translatedMessage = 'speak_nosync'

        elif (re.match('.*enclosure.mouth.events.activate',msg)):
            translatedMessage = 'speak_begin'

        elif (re.match('.*enclosure.mouth.events.deactivate',msg)):
            translatedMessage = 'speak_end'
        
        elif (re.match('.*enclosure.mouth.smile',msg)):
            translatedMessage = 'smile'

        elif (re.match('.*enclosure.mouth.think',msg)):
            translatedMessage = 'think'

        # debug catch-all enclosure activity - TODO remove this
        elif (re.match('.*enclosure',msg)):
            translatedMessage = 'enclosure'

        else:
            translatedMessage = ''

        return translatedMessage


# test
#print(MycroftMap().translate('{"type": "enclosure.mouth.events.activate", "data": {}, "context": {}}'))

'''
# template

        elif (re.match('regex',msg)):
            translatedMessage = 'speak_nosync'




'''