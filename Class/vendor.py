class Vendor:

    def __init__(self, _id=None, name=None, address=None, email=None):
        self.vendorId = _id
        self.vendorName = name
        self.vendorAddress = address
        self.vendorEmail = email

    def get_id(self):
        return self.vendorId

    def get_name(self):
        return self.vendorName

    def get_address(self):
        return self.vendorAddress

    def get_email(self):
        return self.vendorEmail

    def set_name(self, name=None):
        self.vendorName = name

    def set_id(self, _id=None):
        self.vendorId = _id

    def set_address(self, address=None):
        self.vendorAddress = address

    def set_email(self, email=None):
        self.vendorEmail = email
