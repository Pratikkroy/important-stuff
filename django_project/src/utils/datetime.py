import datetime

class DateTime:
    
    @staticmethod
    def current_datetime():
        return datetime.datetime.now()
    
    @staticmethod
    def current_datetime_utc():
        return datetime.datetime.utcnow()