from timeit import default_timer
from time import time


def TicTocGenerator():
    """Generator that returns time differences"""
    ti = 0  # initial time
    tf = time()  # final time
    while True:
        ti = tf
        tf = time()
        yield tf - ti  # returns the time difference


# create an instance of the TicTocGen generator
TTGenerator = TicTocGenerator()


# This will be the main function through which we define both tic() and toc()
def toc(tempBool=True):
    """Prints the time difference yielded by generator instance TTGenerator"""
    tempTimeInterval = next(TTGenerator)
    if tempBool:
        print("Elapsed time: %.3f seconds.\n" % tempTimeInterval)


def tic():
    toc(False)


class TicToc(object):
    """
    Replicate the functionality of MATLAB's tic and toc.

    #Methods
    TicToc.tic()       #start or re-start the timer
    TicToc.toc()       #return and print elapsed time since timer start

    #Attributes
    TicToc.start     #Time from timeit.default_timer() when t.tic() was last called
    TicToc.end       #Time from timeit.default_timer() when t.toc() was last called
    TicToc.elapsed   #t.end - t.start; i.e., time elapsed from t.start when t.toc() was last called
    """

    def __init__(self):
        """Create instance of TicToc class."""
        self.start = float('nan')
        self.end = float('nan')
        self.elapsed = float('nan')

    def tic(self):
        """Start the timer."""
        self.start = default_timer()

    def toc(self, msg='Elapsed time is', restart=False):
        """
        Report time elapsed since last call to tic().

        Returns:
            Time elapsed since last call to tic().

        Optional arguments:
            msg     - String to replace default message of 'Elapsed time is'
            restart - Boolean specifying whether to restart the timer
        """
        self.end = default_timer()
        self.elapsed = self.end - self.start
        print('%s %f seconds.' % (msg, self.elapsed))
        if restart:
            self.start = default_timer()
        return self.elapsed

    def __enter__(self):
        """Start the timer when using TicToc in a context manager."""
        self.start = default_timer()

    def __exit__(self, *args):
        """On exit, printing time elapsed since entering context manager."""
        self.end = default_timer()
        self.elapsed = self.end - self.start
        print('Elapsed time is %f seconds.' % self.elapsed)
