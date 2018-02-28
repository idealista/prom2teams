import sys
import os


try:
    from prom2teams.app.api import app as application
except ImportError:
    sys.path.append(os.path.abspath('./'))
    from prom2teams.app.api import app as application


if __name__ == "__main__":
    application.run()
