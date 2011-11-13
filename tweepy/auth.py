import requests

from tweepy import Error
from tweepy.oauth2 import Consumer, Request, SignatureMethod_HMAC_SHA1, Token

oauth_signature_method = SignatureMethod_HMAC_SHA1()

def oauth_callback(r, consumer, access_token):
    """OAuth authentication callback.

    This will get called by Requests when we need to
    authenticate a new request before it is sent.
    """
    is_form_encoded = isinstance(r.data, list)
    if is_form_encoded:
        parameters = dict(r.data)
        body = None
    else:
        parameters = None
        body = r.data

    request = Request.from_consumer_and_token(consumer,
        token=access_token, http_method=r.method, http_url=r.url,
        parameters=parameters, body=body, is_form_encoded=is_form_encoded)

    request.sign_request(oauth_signature_method, consumer, access_token)

    r.headers.update(request.to_header())
    return r

Basic = 'basic'
OAuth = oauth_callback

class OAuthFlow(object):
    """OAuth flow helper"""

    def __init__(self, consumer, use_https=True, host='api.twitter.com'):
        if isinstance(consumer, tuple):
            self.consumer = Consumer(*consumer)
        else:
            self.consumer = consumer

        self._scheme = 'https' if use_https else 'http'
        self._host = host
        self.session = requests.session(auth=(OAuth, self.consumer, None))

    def _request_token(self, token_type, **param):
        url = '%s://%s/oauth/%s' % (self._scheme, self._host, token_type)
        r = self.session.post(url, headers=param)

        if r.error:
            raise Error('Failed to get OAuth token.', http_error=r.error)

        return Token.from_string(r.content)

    def get_request_token(self, callback='oob', signin_with_twitter=False):
        token = self._request_token('request_token', oauth_callback=callback)
        self.request_token = token

        self.authorization_url = '%s://%s/oauth/%s?%s' % (
            self._scheme, self._host,
            'authenticate' if signin_with_twitter else 'authorize',
            token.to_string())

        return token

    def get_access_token(self, verifier=None):
        if self.request_token is None:
            raise Error('Must get request token first.')
        self.session.auth = (OAuth, self.consumer, self.request_token)

        param = {}
        if verifier:
            param['oauth_verifier'] = verifier
        token = self._request_token('access_token', **param)
        self.access_token = token

        return token

