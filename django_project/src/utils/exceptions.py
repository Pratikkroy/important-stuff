class HttpResponseBadFormatException(Exception):
    '''HttpResponse is in bad format'''
    pass

class ClassShouldNotInstantiateException(Exception):
    ''' Class should not be instantiated '''
    pass

class MethodNotAllowedException(Exception):
    ''' Method is not allowed'''