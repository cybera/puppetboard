from __future__ import absolute_import

import os
import sys

os.environ['PUPPETBOARD_SETTINGS'] = '/srv/puppetboard/puppetboard/settings.py'
activate_this = '/srv/puppetboard/virtenv-puppetboard/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

me = os.path.dirname(os.path.abspath(__file__))
# Add us to the PYTHONPATH/sys.path if we're not on it
if not me in sys.path:
    sys.path.insert(0, me)

from puppetboard.app import app as application
