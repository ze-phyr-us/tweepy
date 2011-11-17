from tweepy import TweepyError

try:
    import simplejson as json
except ImportError, e:
    import json

class Parser(object):

    def parse_content(self, content):
        """Parse the response content and return the a result."""
        raise NotImplementedError

    def parse_error(self, content):
        """Parse the error response and return a message describing it."""
        raise NotImplementedError

class JSONParser(Parser):
    """Parses JSON formatted responses."""

    accepted_formats = ['json']

    def parse_content(self, content):
        try:
            result = json.loads(content)
        except ValueError, e:
            raise TweepyError('JSON parse error: %s\nJSON content:\n%s' % (e, content))

        return result

    def parse_error(self, content):
        error = json.loads(content)
        return error.get('error', 'Unknown: %s' % content)

default_json_parser = JSONParser()

