import socket
from queryBuilder import QueryBuilder
from urllib.parse import urlparse

class Client:

    def get(self,url,verbose):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        parsedUrl = urlparse(url)

        s.connect('www.'+str(parsedUrl.netloc), 80)

        queryParams = str(parsedUrl.path) +'?'+ str(parsedUrl.query)
        query = QueryBuilder('GET', queryParams)
        query.addHeader('Host',str(parsedUrl.netloc))
        query.addHeader('User-Agent', '445Assignment1')
        
        s.sendall(bytes(query.getString(), 'utf8'))

        recBytes = s.recv(4096)
        if(verbose):
            print("".join(map(chr,recBytes)))
        else:
            recBytesSplit = recBytes.split(b'\r\n\r\n')
            print("".join(map(chr,recBytesSplit[1])))
            
        s.close()


    def post(self):