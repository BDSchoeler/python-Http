import socket
from queryBuilder import QueryBuilder

class Client:

    def get(self,url,verbose,headers):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        parsedUrl = url.split('/')

        s.connect('www.'+parsedUrl[2], 80)

        queryParams = parsedUrl[3]
        query = QueryBuilder('GET', queryParams)
        query.addHeader('Host',parsedUrl[2])
        query.addHeader('User-Agent', '445Assignment1')
        for pair in headers:
            query.addHeader(pair[0], pair[1])
        
        s.sendall(bytes(query.getString(), 'utf8'))

        recBytes = s.recv(4096)
        if(verbose):
            print("".join(map(chr,recBytes)))
        else:
            recBytesSplit = recBytes.split(b'\r\n\r\n')
            print("".join(map(chr,recBytesSplit[1])))

        s.close()

    def post(self,url,verbose, body, headers):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        parsedUrl = url.split('/')

        s.connect('www.'+parsedUrl[2], 80)

        queryParams = parsedUrl[3]
        query = QueryBuilder('POST', queryParams)
        query.addHeader('Host',parsedUrl[2])
        query.addHeader('User-Agent', '445Assignment1')
        query.addHeader('Body', body)
        for pair in headers:
            query.addHeader(pair[0], pair[1])
        
        s.sendall(bytes(query.getString(), 'utf8'))

        recBytes = s.recv(4096)
        if(verbose):
            print("".join(map(chr,recBytes)))
        else:
            recBytesSplit = recBytes.split(b'\r\n\r\n')
            print("".join(map(chr,recBytesSplit[1])))

        s.close()