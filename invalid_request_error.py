class InvalidRequest(Exception):

    def __init__(self, message, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = 403
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
