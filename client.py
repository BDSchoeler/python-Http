import socket
from queryBuilder import QueryBuilder

class Client:

    def delete(self, url, verbose, headers, outFile):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        parsedUrl = url.split('/')

        s.connect(('www.'+parsedUrl[2], 80))

        query = self.createQuery('DELETE', parsedUrl, False, headers)
        
        s.sendall(bytes(query.getString(), 'utf8'))

        recBytes = s.recv(4096)
        self.output(recBytes, verbose, outFile)

        s.close()

    def head(self, url, verbose, headers, outFile):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        parsedUrl = url.split('/')

        s.connect(('www.'+parsedUrl[2], 80))

        query = self.createQuery('HEAD', parsedUrl, False, headers)
        
        s.sendall(bytes(query.getString(), 'utf8'))

        recBytes = s.recv(4096)
        self.output(recBytes, verbose, outFile)

        s.close()

    def get(self, url, verbose, headers, outFile):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        parsedUrl = url.split('/')

        s.connect(('www.'+parsedUrl[2], 80))

        query = self.createQuery('GET', parsedUrl, False, headers)
        
        s.sendall(bytes(query.getString(), 'utf8'))

        recBytes = s.recv(4096)
        self.output(recBytes, verbose, outFile)

        s.close()

    def post(self, url, verbose, body, headers, outFile):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        parsedUrl = url.split('/')

        s.connect(('www.'+parsedUrl[2], 80))

        query = self.createQuery('POST', parsedUrl, body, headers)

        s.sendall(bytes(query.getString(), 'utf8'))

        recBytes = s.recv(4096)
        self.output(recBytes, verbose, outFile)

        s.close()

    def put(self, url, verbose, body, headers, outFile):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        parsedUrl = url.split('/')

        s.connect(('www.'+parsedUrl[2], 80))

        query = self.createQuery('PUT', parsedUrl, body, headers)
        s.sendall(bytes(query.getString(), 'utf8'))

        recBytes = s.recv(4096)
        self.output(recBytes, verbose, outFile)

        s.close()

    def createQuery(self, httpType, parsedUrl, body, headers):
        queryParams = parsedUrl[3]
        query = QueryBuilder(httpType, queryParams)
        query.addHeader('Host',parsedUrl[2])
        query.addHeader('User-Agent', 'Concordia-HTTP/1.0')
        query.addHeader('Accept','*/*')
        if(body):
            query.addHeader('Content-Length',str(len(body)))

        for pair in headers:
            query.addHeader(pair[0], pair[1])
        
        query.endOfHeaders()

        if(body):
            query.addBody(body)

        return query

    def output(self, recBytes, verbose, outFile):
        outputString = ''
        if(verbose):
            outputString = outputString.join(map(chr,recBytes))
        else:
            recBytesSplit = recBytes.split(b'\r\n\r\n')
            outputString = outputString.join(map(chr,recBytesSplit[1]))
        
        if(outFile):
            outFile.write(outputString)
            outFile.close()
        else:
            print(outputString)
