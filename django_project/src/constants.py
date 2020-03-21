class UserStatus:
    ACTIVE = 'ACTIVE'
    
class UserGroups:
    ADMIN = 'ADMIN'
    MEMBER = 'MEMBER'
    
class Teams:
    DEFAULT_TEAM = 'DEFAULT_TEAM'
    
class LoginType:
    EMAIL = 'EMAIL'
    PHONE = 'PHONE'
    
class UpdateCredentialsType(LoginType):
    PASSWORD = 'PASSWORD'