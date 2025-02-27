class LoginError(Exception):
    def __init__(self, usr=""):
        super().__init__(self)
        self.usr = usr
    def __str__(self):
        return "LoginError: User '{}' login Failed.".format(self.usr)

class reLoginError(Exception):
    def __init__(self, usr=""):
        super().__init__(self)
        self.usr = usr
    def __str__(self):
        return "ReLoginError: User '{}' relogin Failed.".format(self.usr)

class configError(Exception):
    def __init__(self, errorInfo=""):
        super().__init__(self)
        self.errorInfo = errorInfo
    def __str__(self):
        return "ConfigError: {}.".format(self.errorInfo)

class bookError(Exception):
    def __init__(self):
        super().__init__(self)
    def __str__(self):
        return "BookError: Book Failed."

if __name__=='__main__':
    try:
        raise bookError()
    except Exception as e:
        print(str(e))