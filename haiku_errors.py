# -*- coding: utf-8 -*-
"""
Haiku sources:

 [1]: https://camtools.cam.ac.uk/wiki/site/5b59f819-0806-4a4d-0046-bcad6b9ac70f/haiku%20error%20messages.html
 [2]: http://baetzler.de/humor/haiku_error.var
 [3]: https://scs.senecac.on.ca/~timothy.mckenna/offline/Haikus.htm
 [4]: http://members.tripod.com/martin_leese/haiku.html

"""  # noqa
VERSION = (0, 3, 0)  # PEP 386  # noqa
__version__ = ".".join([str(x) for x in VERSION])  # noqa

import sys
from random import choice
from collections import defaultdict

try:  # note: py2 compat
    FileNotFoundError
except NameError:
    FileNotFoundError = OSError

try:  # note: py3 compat
    EnvironmentError
except NameError:
    EnvironmentError = OSError

try:  # note: Windows/Linux compat
    WindowsError
except NameError:
    WindowsError = OSError

try:
    RecursionError
except NameError:
    RecursionError = RuntimeError


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
    """
    A crash reduces
    your expensive computer
    to a simple stone.
    ~ (James Lopez)
    """,  # [^4]
)

_HAIKUS = defaultdict(list)

_HAIKUS[FileNotFoundError].extend([
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
    Three things are certain:
    Death, taxes, and lost data.
    Guess which has occurred.
    ~ (David Dixon)
    """,  # [^1]
])

_HAIKUS[IOError].extend([
    """
    Spring will come again,
    But it will not bring with it
    Any of your files.
    ~ (Cheryl Walker)
    """,  # [^2]
])

_HAIKUS[MemoryError].extend([
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
])

_HAIKUS[LookupError].extend([
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
])

_HAIKUS[SyntaxError].extend([
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
])

_HAIKUS[EnvironmentError].extend([
    """
    New hardware was found.
    Please insert new driver disk.
    Could have bought a MAC.
    ~ (unknown)
    """,  # [^2]
])

_HAIKUS[KeyboardInterrupt].extend([
    """
    No keyboard present
    Hit F1 to continue
    Zen engineering?
    ~ (Jim Griffith)
    """,  # [^4]
])

_HAIKUS[ZeroDivisionError].extend([
    """
    Infinity is
    Attainable when users
    Divide by zero
    ~ (unknown)
    """,  # [^2]
])

_HAIKUS[SystemError].extend([
    """
    Something has gone wrong.
    Format your disk, because this
    Error won't help you.
    ~ (Cheryl Walker)
    """,  # [^2]
])

_HAIKUS[RuntimeError].extend([
    """
    Yesterday it worked.
    Today it is not working.
    Windows is like that.
    ~ (Margaret Segall)
    """,  # [^1]
])

_HAIKUS[TypeError].extend([
    """
    Something you entered
    transcended parameters.
    So much is unknown.
    ~ (unknown)
    """,  # [^2]
])


_HAIKUS[RecursionError].extend([
    """
    Fatal exception.
    Code has looped upon itself
    like the coiled serpent.
    ~ (Loren DeLaOsa)
    """,  # [^2]
])


_HAIKUS[WindowsError].extend([
    """
    Windows NT crashed.
    I am the Blue Screen of Death.
    No one hears your screams.
    ~ (Peter Rothman)
    """,  # [^2]
    """
    Yesterday it worked.
    Today it is not working
    Windows is like that.
    ~ (Margaret Segall)
    """,  # [^2]
])


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
    sys.__excepthook__(exctype, value, traceback)

    print_haiku(exctype=exctype, value=value)

sys.excepthook = haiku_excepthook
