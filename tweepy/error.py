# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

from six import text_type


class TweepError(Exception):
    """Tweepy exception"""

    def __init__(self, reason, response=None):
        self.reason = text_type(reason)
        self.response = response
        Exception.__init__(self, reason)

    def __str__(self):
        return self.reason

