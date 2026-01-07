# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (X self, X cls)

class Connection:

    def __init__(self, host='hostname'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self,user):
        self.user = user
    
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_user_auth(cls, user, password):
        connection = cls()
        connection.set_user(user) # ou set_user('teste')
        connection.set_password(password) # ou set_passworld('1234') 
        return connection
    
    # Um metodo estático, te dá a possíbilidade de chamar a função a partir da classe ao invés da instancia
    @staticmethod
    def log(msg):
        # No metros static não pode utilizar nem o self nem o cls
        return msg
        
    


c1 = Connection()
c1.set_user('user')
c1.set_password('1234')

print(c1.user)
print(c1.password)

c2 = Connection.create_user_auth('user2', '1234')

print(c2.user)
print(c2.password)

print("LOG: ", Connection.log("ISSO É UMA MENSAGEM DE LOG"))