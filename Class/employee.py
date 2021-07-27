class Employee:
    def __init__(self, name=None, userName=None, password=None, id=None):
        self.name = name
        self.id = id
        self.password = password
        self.userName = userName
        self.empCode = 0


#0 for normal employee,1 for sales clerk , 2 for manager, 3 for owner
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_username(self):
        return self.userName

    def set_username(self, userName):
        self.userName = userName

    def get_password(self):
        return self.password


    def set_password(self, password):
        self.password = password


    def get_empcode(self):
        return self.empCode


    def set_empcode(self, empCode):
        self.empCode = empCode

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
