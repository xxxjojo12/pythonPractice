from glob import glob
from sys import _enablelegacywindowsfsencoding


def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)