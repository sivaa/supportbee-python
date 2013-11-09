# -*- coding: utf-8 -*-

import requests


class SupportBee(object):
    BASE_URL = "https://%s.supportbee.com/" 
    
    def __init__(self, account_name, auth_token):
        """
        Initialize with Account Name and Auth Token.
        Auth Token can be found at https://<Account Name>.supportbee.com/users/<User ID>/settings/api_token
        """
        self.account_name = account_name
        self.auth_token = auth_token
        self.url = SupportBee.BASE_URL % self.account_name
        
    def _request(self, url_slug, params):
        params['auth_token'] = self.auth_token
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        r = requests.get('%s%s' % (self.url, url_slug), params=params, headers=headers)
        return r.json()
    
    def fetch_tickets(self, **kwargs):
        """
        Supported parameters are available at https://developers.supportbee.com/api#fetching_tickets 
        """
        return self._request('/tickets.json', kwargs)
