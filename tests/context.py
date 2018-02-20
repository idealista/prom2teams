import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../prom2teams')))
from prom2teams import server, exceptions
from prom2teams.message.alarm_mapper import AlarmMapper
