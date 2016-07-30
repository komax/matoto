#!/usr/bin/env python
"""
A simple timer for various activities such as pomodoros, breaks, mindfulness
exercises.
"""

import time
import os
import sys

class Activity(object):
    def __init__(self, greeting, duration):
        self._greeting = greeting
        self._duration = duration

    def __call__(self):
        print(self._greeting)
        time.sleep(self._duration)
        class_name = self.__class__.__name__
        notification_msg =\
            "You finished activity %s in %i seconds. Well done!" %\
                (class_name, self._duration)
        os.system('aplay -q bell-outside.wav')
        print(notification_msg)
        os.system('notify-send "%s"' % notification_msg)


class Pomodoro(Activity):
    """
    Start a pomodoro with as many seconds as given from duration.
    The default is 1500 seconds, 25 minutes
    """
    def __init__(self, duration=1500):
        super().__init__("Starting a pomodoro. Get prepared to work.",
                duration)


class Break(Activity):
    """
    Start a break of 5 minutes as default or supply a different duration
    """
    def __init__(self, duration=300):
        super().__init__("Now it is time for a break! Relax.", duration)


def create_activity(user_choice):
    if user_choice == 'b':
        activity = Break()
    elif user_choice == 'p':
        activity = Pomodoro()
    else:
        raise ValueError("Cannot create an activity from this user choice '%s'"
                % user_choice)
    return activity


def process_user_input():
    try:
        while True:
            user_input = ''
            while len(user_input) != 1 and user_input not in ['b', 'p', 'q']:
                user_input = input(
                        "Please enter your activity: [p] for starting a "+
                        "pomodoro, [b] for starting a break OR [q]uit > ")
            if user_input == 'q':
                raise EOFError
            activity = create_activity(user_input)
            activity()
    except EOFError:
        print("\nExiting matoto.")
        sys.exit(0)


def run_matoto():
    process_user_input()


if __name__ == '__main__':
    run_matoto()
