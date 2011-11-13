import requests
from urlparse import urljoin

from tweepy import Error

class Client(object):

    def __init__(self, auth=None, host='api.twitter.com', secure=True, api_version='1'):
        self.base_url = '%s://%s/%s' % ('https' if secure else 'http', host, api_version)
        self.session = requests.session(auth=auth) if auth else requests

    def request(self, method, url, parameters=None):
        """Send a request to API server.

        method: type of HTTP method to send (ex: GET, DELETE, POST)
        url: API endpoint URL minus the /<version> part.
        parameters: API parameters to be sent with the request.
        """
        url = urljoin(self.base_url, url) + '.json'
        r = self.session.request(method, url, data=parameters)

        if r.error:
            print 'HTTPError: ' + str(r.error)
            raise Error('API request failed. URL=%s' % url, http_error=r.error)

        # TODO: parse response
        return r.content

    def public_timeline(self, **parameters):
        """GET statuses/public_timeline"""
        return self.request('GET', 'statuses/public_timeline', parameters)

    def update_status(self, status, **parameters):
        """POST statuses/update"""
        parameters.update({'status': status})
        return self.request('POST', 'statuses/update', parameters)

