import timer
import os


class Activity(object):
    def __init__(greeting):
        self._greeting = greeting

    def __call__(duration):
        print(self._greeting)
        timer.sleep(duration)
        class_name = self.__class__.__name__
        notification_msg =\
            "You finished activity %s in %i seconds. Well done!" %\
                (class_name, duration)
        print(notification_msg)
        os.system('notify-send "%s"' % notification_msg)


class Pomodoro(Activity):
    def __init__():
        super().__init__("Starting a pomodoro. Get prepared to work.")

    def __call__(duration=1500):
        """
        Start a pomodoro with as many seconds as given from duration.
        The default is 1500 seconds, 25 minutes
        """
        self(duration)


class Break(Activity):
    def __init__():
        super().__init__("Now it is time for a break! Relax.")

    def __call__(duration=300):
        """
        Start a break of 5 minutes as default or supply a different duration
        """
        self(duration)


def run_matoto():
    pass


if __name__ == '__main__':
    run_matoto()
