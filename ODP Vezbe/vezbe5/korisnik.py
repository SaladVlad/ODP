class Korisnik:

    def __init__(self,user,passwd,roles=[]):
        self.user = user
        self.passwd = passwd
        self.auth = False
        self.roles = roles