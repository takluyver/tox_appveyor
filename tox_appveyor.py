"""Select 32 or 64-bit Python for Tox on Appveyor

Set the environment variable TOX_APPVEYOR_X64=1 for 64-bit Python.
Unset, or set to 0, Tox will use a 32-bit (x86) Python build.
"""
import os
import re
import tox
from warnings import warn

__version__ = '0.1.1'

@tox.hookimpl
def tox_get_python_executable(envconfig):
    x64_suffix = ''

    X64_ENV = os.environ.get('TOX_APPVEYOR_X64', '')
    if X64_ENV == '1':
        x64_suffix = '-x64'
    elif X64_ENV not in ('0', ''):
        warn("TOX_APPVEYOR_X64 environment variable should be '0' or '1' if set. "
             "Ignoring value %r" % X64_ENV, UserWarning)

    m = re.match(r'python(\d)\.(\d)', envconfig.basepython)
    if not m:
        # Requested Python not in the format we expect; let other
        # hook implementations try to find it.
        return None

    major, minor = m.groups()

    exe_path = 'C:\\Python{}{}{}\\Python.exe'.format(major, minor, x64_suffix)
    if os.path.isfile(exe_path):
        return exe_path
    else:
        warn("{!r} does not exist".format(exe_path), UserWarning)
        return None
