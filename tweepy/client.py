from urlparse import urljoin

import requests

class Client(object):

    def __init__(self, auth=None, host='api.twitter.com', secure=True, api_version='1'):
        self.base_url = '%s://%s/%s' % ('https' if secure else 'http', host, api_version)
        self.session = requests.session(auth=auth) if auth else requests

    def request(self, method, url, options=None):
        """Send a request to API server.

        method: type of HTTP method to send (ex: GET, DELETE, POST)
        url: API endpoint URL minus the /<version> part.
        options: additonal optional options available to any API endpoint.
        """
        url = urljoin(self.base_url, url) + '.json'
        resp = self.session.request(method, url)

        if resp.ok is False:
            resp.raise_for_status()

        return resp.content

    def public_timeline(self, **options):
        """GET statuses/public_timeline"""
        return self.request('GET', 'statuses/public_timeline', options)

