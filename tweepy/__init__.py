__version__ = '2.0'
__author__ = 'Joshua Roesslein'
__license__ = 'MIT'

class Error(RuntimeError):
    """Tweepy generic error"""

    def __init__(self, message, http_error=None):
        self._message = message
        self._http_error = http_error

    @property
    def message(self):
        """A hack to get around the deprecation errors in 2.6."""
        return self._message

    @property
    def http_error(self):
        return self._http_error

    def __str__(self):
        return self._message

