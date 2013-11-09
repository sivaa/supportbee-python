# -*- coding: utf-8 -*-

from supportbee.exceptions import ValidationFailureException, \
    UnAuthorizedException, AccessDeniedException, ClientException, \
    ServerFailureException, ServerException, SupportBeeException
import requests
import json

class SupportBee(object):
    BASE_URL = "https://%s.supportbee.com" 
    
    def __init__(self, account_name, auth_token):
        """
        Initialize with Account Name and Auth Token.
        Auth Token can be found at https://<Account Name>.supportbee.com/users/<User ID>/settings/api_token
        """
        self.account_name = account_name
        self.auth_token = auth_token
        self.url = SupportBee.BASE_URL % self.account_name
        
    def _raise_exception(self, response):
        if 400 <= response.status_code < 500:
            if response.status_code == 400:
                raise ValidationFailureException(response.status_code, response.reason)
            elif response.status_code == 401:
                raise UnAuthorizedException(response.status_code, response.reason, response=response)
            elif response.status_code == 403:
                raise AccessDeniedException(response.status_code, response.reason)
            else:
                raise ClientException(response.status_code, response.reason)
        elif 500 <= response.status_code < 600:
            if response.status_code == 500:
                raise ServerFailureException(response.status_code, response.reason)
            else:
                raise ServerException(response.status_code, response.reason)
    
    def _request(self, url_slug, params={}, method='GET'):
        params['auth_token'] = self.auth_token
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        if method.upper() == 'GET':
            r = requests.get('%s%s' % (self.url, url_slug), params=params, headers=headers)
        elif method.upper() == 'POST':
            r = requests.post('%s%s' % (self.url, url_slug), data=json.dumps(params), headers=headers)
        elif method.upper() == 'DELETE':
            r = requests.delete('%s%s' % (self.url, url_slug), params=params, headers=headers)
        else:
            raise SupportBeeException("Unsupported Request")

        if r.ok and not r.status_code == 204:
            return r.json()

        self._raise_exception(r)
        
    def fetch_tickets(self, **kwargs):
        """
        Supported parameters are available at https://developers.supportbee.com/api#fetching_tickets 
        """
        return self._request('/tickets.json', kwargs)

    def create_ticket(self, data):
        """
        Supported data as dictionary. Valid options are available at https://developers.supportbee.com/api#create_ticket 
        """
        return self._request('/tickets.json', data, 'post')

    def show_ticket(self, ticket_id):
        """
        Fetch the given ticket. Supported parameters are available at https://developers.supportbee.com/api#show_ticket
        Params
            ticket_id: SuppportBee Ticket ID
        """
        return self._request('/tickets/%s.json' % (ticket_id))

    def archive_ticket(self, ticket_id):
        """
        Archives the given ticket. Supported parameters are available at https://developers.supportbee.com/api#ticket_actions
        Params
            ticket_id: SuppportBee Ticket ID
        """
        return self._request('/tickets/%s/archive.json' % (ticket_id), method='POST')


    def unarchive_ticket(self, ticket_id):
        """
        Unarchives the given ticket. Supported parameters are available at https://developers.supportbee.com/api#ticket_actions
        Params
            ticket_id: SuppportBee Ticket ID
        """
        return self._request('/tickets/%s/archive.json' % (ticket_id), method='DELETE')

    def assign_ticket(self, tickect_id, data):
        """
        Supported data as dictionary. Valid options are available at https://developers.supportbee.com/api#ticket_actions 
        Params
            ticket_id: SuppportBee Ticket ID
            data     : JSON/Dict represents the User/Group ID
        """
        return self._request( '/tickets/%s/assignments.json' % (tickect_id) , data, 'post')

    def star_ticket(self, ticket_id):
        """
        Stars the given ticket. Supported parameters are available at https://developers.supportbee.com/api#ticket_actions
        Params
            ticket_id: SuppportBee Ticket ID
        """
        return self._request('/tickets/%s/star.json' % (ticket_id), method='POST')


    def unstar_ticket(self, ticket_id):
        """
        Unstars the given ticket. Supported parameters are available at https://developers.supportbee.com/api#ticket_actions
        Params
            ticket_id: SuppportBee Ticket ID
        """
        return self._request('/tickets/%s/star.json' % (ticket_id), method='DELETE')


    def spam_ticket(self, ticket_id):
        """
        Spams the given ticket. Supported parameters are available at https://developers.supportbee.com/api#ticket_actions
        Params
            ticket_id: SuppportBee Ticket ID
        """
        return self._request('/tickets/%s/spam.json' % (ticket_id), method='POST')


    def unspam_ticket(self, ticket_id):
        """
        Un-spam the given ticket. Supported parameters are available at https://developers.supportbee.com/api#ticket_actions
        Params
            ticket_id: SuppportBee Ticket ID
        """
        return self._request('/tickets/%s/spam.json' % (ticket_id), method='DELETE')


    def trash_ticket(self, ticket_id):
        """
        Trashes the given ticket. Supported parameters are available at https://developers.supportbee.com/api#ticket_actions
        Params
            ticket_id: SuppportBee Ticket ID
        """
        return self._request('/tickets/%s/trash.json' % (ticket_id), method='POST')


    def untrash_ticket(self, ticket_id):
        """
        Un-trashes the given ticket. Supported parameters are available at https://developers.supportbee.com/api#ticket_actions
        Params
            ticket_id: SuppportBee Ticket ID
        """
        return self._request('/tickets/%s/trash.json' % (ticket_id), method='DELETE')

    def fetch_replies(self, ticket_id):
        """
        Fetches all the replies for the given ticket. More details are available at https://developers.supportbee.com/api#fetching_replies 
        """
        return self._request('/tickets/%s/replies.json' % (ticket_id))

    def create_reply(self, ticket_id, data):
        """
        Supported data as dictionary. Valid options are available at https://developers.supportbee.com/api#create_reply 
        """
        return self._request('/tickets/%s/replies.json' % (ticket_id), data, 'post')

    def show_reply(self, ticket_id, reply_id):
        """
        Fetches the reply for the given ticket & reply Id. Supported parameters are available at https://developers.supportbee.com/api#show_reply
        Params
            ticket_id: SuppportBee Ticket ID
            reply_id: Reply Id
        """
        return self._request('/tickets/%s/replies/%s.json' % (ticket_id, reply_id))

