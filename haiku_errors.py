# -*- coding: utf-8 -*-
"""
references:

 [1]: https://camtools.cam.ac.uk/wiki/site/5b59f819-0806-4a4d-0046-bcad6b9ac70f/haiku%20error%20messages.html
 [2]: http://baetzler.de/humor/haiku_error.var
 [3]: https://scs.senecac.on.ca/~timothy.mckenna/offline/Haikus.htm

"""  # noqa

import sys
from random import choice

_HAIKU_FALLBACKS = (
    """
    To have no errors
    Would be life without meaning
    No struggle, no joy
    ~ (Brian M. Porter)
    """,  # [^1]
    """
    Errors have occurred.
    We won't tell you where or why.
    Lazy programmers.
    ~ (Charlie Gibbs)
    """,  # [^1]
    """
    The code was willing,
    It considered your request,
    But the chips were weak.
    ~ (Barry L. Brumitt)
    """,  # [^1]
)

_HAIKUS = {
    IOError: (
        """
        Hal, open the file
        Hal, open the damn file, Hal
        open the, please Hal
        ~ (Jennifer Jo Lane)
        """,  # [^1]
        """
        Having been erased,
        The document you’re seeking
        Must now be retyped.
        ~ (Judy Birmingham)
        """,  # [^1]
        """
        A file that big?
        It might be very useful.
        But now it is gone.
        ~ (David J. Liszewski)
        """,  # [^1]
        """
        Rather than a beep
        Or a rude error message,
        These words: “File not found.”
        ~ (Len Dvorkin)
        """,  # [^1]
        """
        Spring will come again,
        But it will not bring with it
        Any of your files.
        ~ (Cheryl Walker)
        """,  # [^2]
    ),
    MemoryError: (
        """
        I'm sorry, there's um
        insufficient -- what's-it-called?
        The term eludes me…
        ~ (Owen Mathews)
        """,  # [^1]
        """
        Out of memory.
        We wish to hold the whole sky,
        But we never will.
        ~ (Francis Heaney)
        """,  # [^1]
        """
        Memory shaken,
        The San Andreas of all
        Invalid page faults.
        ~ (Cheryl Walker)
        """,  # [^2]
    ),
    LookupError: (
        """
        ABORTED effort.
        Close all that you have.
        You ask way too much.
        ~ (Mike Hagler)
        """,  # [^1]
        """
        The ten thousand things,
        How long do any persist?
        Netscape, too, has gone.
        ~ (Jason Willoughby)
        """,  # [^1]
    ),
    KeyboardInterrupt: (
        """
        No keyboard present
        Hit F1 to continue
        Zen engineering?
        ~ (Jim Griffith)
        """,  # [^1]
    ),
    SyntaxError: (
        """
        Seeing my great fault
        Through darkening blue windows
        I begin again
        ~ (Chris Walsh)
        """,  # [^1]
        """
        Expression police!
        An illegal expression
        Has been committed.
        ~ (unknown)
        """,  # [^2]
    ),
    OSError: (
        """
        New hardware was found.
        Please insert new driver disk.
        Could have bought a MAC.
        ~ (unknown)
        """,  # [^2]
    ),
    ZeroDivisionError: (
        """
        Infinity is
        Attainable when users
        Divide by zero
        ~ (unknown)
        """,  # [^2]
    ),
    SystemError: (
        """
        Something has gone wrong.
        Format your disk, because this
        Error won't help you.
        ~ (Cheryl Walker)
        """,  # [^2]
    ),
    RuntimeError: (
        """
        Yesterday it worked.
        Today it is not working.
        Windows is like that.
        ~ (Margaret Segall)
        """,  # [^1]
    ),
    TypeError: (
        """
        Something you entered
        transcended parameters.
        So much is unknown.
        ~ (unknown)
        """,  # [^2]
    )
}


def print_haiku(exctype, value, indent=4):
    for klass in exctype.__mro__:
        if klass in _HAIKUS:
            haiku = choice(_HAIKUS[klass])
            break
    else:  # nobreak
        haiku = choice(_HAIKU_FALLBACKS)

    for line in haiku.format(exctype=exctype, value=value).split('\n'):
        print(" " * indent + line.strip())


def haiku_excepthook(exctype, value, traceback):
    print_haiku(exctype=exctype, value=value)

    sys.__excepthook__(exctype, value, traceback)


sys.excepthook = haiku_excepthook
