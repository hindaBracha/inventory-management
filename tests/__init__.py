import sys
from unittest.mock import MagicMock

sys.modules['celery'] = MagicMock()
