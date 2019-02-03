class QueryBuilder:
    def __init__(self, httpType, queryParams):
        self.string =  httpType + ' /' + queryParams + ' HTTP/1.1\r\n'

    def addHeader(self, headerName, headerContent):
        self.string += headerName + ': ' + headerContent +'\r\n'

    def getString(self):
        self.string += '\r\n'
        return self.string