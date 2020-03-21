import jwt
from jwt import InvalidSignatureError, ExpiredSignatureError, DecodeError
from settings.base import SECRET_KEY
from .settings import SIMPLE_JWT
from src.utils.datetime import DateTime
from src.utils import HttpStatus, HttpResponse


class JWTToken:
    
    @staticmethod
    def _decode_token(token):
        try:
            return jwt.decode(
                token, 
                SIMPLE_JWT['SIGNING_KEY'], 
                leeway=SIMPLE_JWT['LEEWAY_TIME'], 
                algorithms=SIMPLE_JWT['ALGORITHM']
            )
        except (InvalidSignatureError, DecodeError):
            return HttpResponse(http_status=HttpStatus.HTTP_401_UNAUTHORIZED,
                data="TOKEN_INVALID")
        except ExpiredSignatureError:
            return HttpResponse(http_status=HttpStatus.HTTP_401_UNAUTHORIZED,
                data="TOKEN_EXPIRED")
            
            
    @staticmethod   
    def _encode_token(payload, token_lifetime):
        payload.update(exp=DateTime.current_datetime_utc()+token_lifetime)
        return jwt.encode(
            payload, 
            SIMPLE_JWT['SIGNING_KEY'], 
            algorithm=SIMPLE_JWT['ALGORITHM']
        ).decode("utf-8") 
        


  
class Token(JWTToken):
    @staticmethod
    def get_token(payload):
        access_token = JWTToken._encode_token(payload, token_lifetime=SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'])
        payload.update(access_token=access_token)
        refresh_token = JWTToken._encode_token(payload=payload,token_lifetime=SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'])
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
    
    @staticmethod
    def get_claims(token):
        return JWTToken._decode_token(token)
    
    @staticmethod
    def refresh_token(access_token, refresh_token):
        response = JWTToken._decode_token(refresh_token)
        if isinstance(response, HttpResponse):
            return response
        
        if response['access_token'] == access_token:
            return Token.get_token({'auth_id':response['auth_id']})
        else:
            return HttpResponse(http_status=HttpStatus.HTTP_401_UNAUTHORIZED,
                data="TOKEN_INVALID")
    
    