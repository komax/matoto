#!/usr/bin/env python
"""
A simple timer for various activities such as pomodoros, breaks, mindfulness
exercises.
"""

import os
import sys
import time


def time_function(func):
    """
    Profiles a function call and returns the seconds that it took to complete
    the call.
    :param func: a function/method/closure to call without any parameters
    :return: competition time in seconds.
    """
    start = time.time()
    func()
    end = time.time()
    return end - start


class Activity(object):
    """
    Generalizes behavior for all different activities, such as pomodoro, break.
    It is a command object with a default implementation to execute the
    activity.
    """

    def __init__(self, greeting, duration, mute=False):
        self._greeting = greeting
        self._duration = duration
        self._mute = mute

    def __call__(self):
        print(self._greeting)
        time.sleep(self._duration)
        activity_name = self.__class__.__name__.lower()
        notification_msg = \
            "You finished a %s in %i seconds. Well done!" % \
            (activity_name, self._duration)
        print(notification_msg)
        os.system('notify-send "%s"' % notification_msg)
        if self._mute:
            os.system('aplay -q bell-outside.wav')


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
    """
    Factory to create different types of activities.
    :param user_choice: a str of length 1 to describe the type of the object.
    :return: a freshly created activity.
    """
    if user_choice == 'b':
        activity = Break()
    elif user_choice == 'p':
        activity = Pomodoro()
    else:
        raise ValueError("Cannot create an activity from this user choice '%s'"
                         % user_choice)
    return activity


def get_user_input():
    try:
        user_input = ''
        while len(user_input) != 1 and user_input not in ['b', 'p', 'q']:
            user_input = input(
                "Please enter your activity: [p] for starting a " +
                "pomodoro, [b] for starting a break OR [q]uit > ")
            user_input = user_input.lower()
        # Return the correct choices.
        return user_input
    except EOFError:
        return 'q'


def run_matoto():
    user_input = get_user_input()
    while user_input != 'q':
        activity = create_activity(user_input)
        activity()
        user_input = get_user_input()
    # User wants to quit. Quit the program.
    print("\nExiting matoto.")
    sys.exit(0)


if __name__ == '__main__':
    run_matoto()

