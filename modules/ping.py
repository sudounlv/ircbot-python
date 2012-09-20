#!/usr/bin/env python
"""
ping.py - Phenny Ping Module
Author: Sean B. Palmer, inamidst.com
About: http://inamidst.com/phenny/
"""

import random

def hello(phenny, input): 
   greeting = random.choice(('Hi', 'Hey', 'Hello'))
   punctuation = random.choice(('', '!'))
   phenny.say(greeting + ' ' + input.nick + punctuation)
hello.rule = r'(?i)(hi|hello|hey) $nickname[ \t]*$'

def interjection(phenny, input): 
   phenny.say(input.nick + '!')
interjection.rule = r'$nickname!' # $nickname = global var for uer's nick for phenny
interjection.priority = 'high'
interjection.thread = False

if __name__ == '__main__': 
   print __doc__.strip()


def hello_world(phenny, input):
    phenny.say("Hello World!")
hello_world.commands = ['hello']
hello_world.priority = 'medium'


def custom_commands(phenny, input):
    if input.sender.startswith('#'): return
    names = ', '.join(sorted(phenny.doc.iterkeys()))
    phenny.say('Commands I recognise: ' + names + '.')
    phenny.say(("For help, do '%s: help example?' where example is the " + 
               "name of the command you want help for.") % phenny.nick)
custom_commands.rule = r'!help $nickname'
custom_commands.priority = 'low'
