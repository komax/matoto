#!/usr/bin/env python
"""
A simple timer for various activities such as pomodoros, breaks, mindfulness
exercises.
"""

import timer
import os
import sys

class Activity(object):
    def __init__(greeting, duration=None):
        self._greeting = greeting
        self._duration = duration

    def __call__():
        print(self._greeting)
        timer.sleep(self._duration)
        class_name = self.__class__.__name__
        notification_msg =\
            "You finished activity %s in %i seconds. Well done!" %\
                (class_name, self._duration)
        print(notification_msg)
        os.system('notify-send "%s"' % notification_msg)


class Pomodoro(Activity):
    """
    Start a pomodoro with as many seconds as given from duration.
    The default is 1500 seconds, 25 minutes
    """
    def __init__():
        super().__init__("Starting a pomodoro. Get prepared to work.",
                duration=1500)

    def __call__():
        self(duration)


class Break(Activity):
    """
    Start a break of 5 minutes as default or supply a different duration
    """
    def __init__():
        super().__init__("Now it is time for a break! Relax.", duration=300)

    def __call__():
        self(duration)


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
            while len(user_input) != 1 and user_input not in ['b', 'p']:
                user_input = input("""
                    Please enter your activity: [p] for starting a pomodoro OR
                    [b] for starting a break >
                    """)
            activity = create_activity(user_input)
            activity()
    except EOFError:
        print("Exiting matoto.")
        sys.exit(0)


def run_matoto():
    pass


if __name__ == '__main__':
    run_matoto()
