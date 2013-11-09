# -*- coding: utf-8 -*-

class SupportBeeException(IOError):
    """
    There was an exception that occurred while handling your SupportBee request.
    """
    def __init__(self, msg):
        self.msg = msg
        
    def __unicode__(self):
        return self.msg

    def __repr__(self):
        return self.__unicode__()
    
    def __str__(self):
        return self.__unicode__()

class ClientException(SupportBeeException):
    def __init__(self, status_code, msg):
        self.status_code = status_code
        self.msg = msg
    
    def __unicode__(self):
        return u'%s : %s' % (self.status_code, self.msg) 

class ServerException(SupportBeeException):
    def __init__(self, status_code, msg):
        self.status_code = status_code
        self.msg = msg
    
    def __unicode__(self):
        return u'%s : %s' % (self.status_code, self.msg) 

class ServerFailureException(ServerException):    
    def __init__(self, *args, **kwargs):
        """ Initializes FailureException with optional `response` object. """
        self.response = kwargs.pop('response', None)
        super(ServerFailureException, self).__init__(*args, **kwargs)

class ValidationFailureException(ClientException):    
    def __init__(self, *args, **kwargs):
        """ Initializes ValidationFailureException with optional `response` object. """
        self.response = kwargs.pop('response', None)
        super(ValidationFailureException, self).__init__(*args, **kwargs)

class UnAuthorizedException(ClientException):    
    def __init__(self, *args, **kwargs):
        """ Initializes UnAuthorizedException with optional `response` object. """
        self.response = kwargs.pop('response', None)
        super(UnAuthorizedException, self).__init__(*args, **kwargs)

class AccessDeniedException(ClientException):    
    def __init__(self, *args, **kwargs):
        """ Initializes AccessDeniedException with optional `response` object. """
        self.response = kwargs.pop('response', None)
        super(AccessDeniedException, self).__init__(*args, **kwargs)
