class Publisher:
    def __init__(self, Id=0, pName=None, vndr=None):
        self.publisherId = Id
        self.publisherName = pName
        self.vendor = vndr

    def get_publisherId(self):
        return self.publisherId

    def set_publisherId(self, Id):
        self.publisherId = Id

    def get_publisherName(self):
        return self.publisherName

    def set_publisherName(self, pName):
        self.publisherName = pName

    def get_vendor(self):
        return self.vendor

    def set_vendor(self, vndr):
        self.vendor = vndr
