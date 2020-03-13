import uuid
class Utility(object):
    
    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())