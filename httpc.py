import click
from client import Client 

@click.group()
def cli():
    """httpc is a curl-like application but supports HTTP protocol only."""
    pass

@cli.command()
@click.argument('url', type=str, required=True)
@click.option('-h', '--header', multiple=True, help='key:value Associates headers to HTTP Request with the format.')
@click.option('-o', '--output', type=click.File('w'), help='Creates a file and writes the output into the file.')
@click.option('-v', '--verbose', is_flag=True, help='Prints the detail of the response such as protocol, status, and headers.')
def get(url, header, output, verbose):
    '''executes a HTTP GET request and prints the response.'''
    client = Client()

    headers = []
    for pair in header:
        headers.append(pair.split(':'))

    client.get(url, verbose, headers, output)

@cli.command()
@click.argument('url', type=str, required=True)
@click.option('-d', '--data', type=str, help='Associates an inline data to the body HTTP POST request.')
@click.option('-f', '--file', type=click.File('r'), help='Associates the content of a file to the body HTTP POST request.')
@click.option('-h', '--header', multiple=True, help='key:value Associates headers to HTTP Request with the format.')
@click.option('-o', '--output', type=click.File('w'), help='Creates a file and writes the output into the file.')
@click.option('-v', '--verbose', is_flag=True, help='Prints the detail of the response such as protocol, status, and headers.')
def post(url, data, file, header, output, verbose):
    '''executes a HTTP POST request and prints the response.'''
    client = Client()
    body = ''

    if data:
        body = data
    elif file:
        body = file.read()

    headers = []
    for pair in header:
        headers.append(pair.split(':'))

    client.post(url, verbose, body, headers, output)

@cli.command()
@click.argument('url', type=str, required=True)
@click.option('-d', '--data', type=str, help='Associates an inline data to the body HTTP POST request.')
@click.option('-f', '--file', type=click.File('r'), help='Associates the content of a file to the body HTTP POST request.')
@click.option('-h', '--header', multiple=True, help='key:value Associates headers to HTTP Request with the format.')
@click.option('-o', '--output', type=click.File('w'), help='Creates a file and writes the output into the file.')
@click.option('-v', '--verbose', is_flag=True, help='Prints the detail of the response such as protocol, status, and headers.')
def put(url, data, file, header, output, verbose):
    '''executes a HTTP PUT request and prints the response.'''
    client = Client()
    body = ''

    if data:
        body = data
    elif file:
        body = file.read()

    headers = []
    for pair in header:
        headers.append(pair.split(':'))

    client.put(url, verbose, body, headers, output)

@cli.command()
@click.argument('url', type=str, required=True)
@click.option('-h', '--header', multiple=True, help='key:value Associates headers to HTTP Request with the format.')
@click.option('-o', '--output', type=click.File('w'), help='Creates a file and writes the output into the file.')
@click.option('-v', '--verbose', is_flag=True, help='Prints the detail of the response such as protocol, status, and headers.')
def delete(url, header, output, verbose):
    '''executes a HTTP DELETE request and prints the response.'''
    client = Client()

    headers = []
    for pair in header:
        headers.append(pair.split(':'))

    client.delete(url, verbose, headers, output)

@cli.command()
@click.argument('url', type=str, required=True)
@click.option('-h', '--header', multiple=True, help='key:value Associates headers to HTTP Request with the format.')
@click.option('-o', '--output', type=click.File('w'), help='Creates a file and writes the output into the file.')
@click.option('-v', '--verbose', is_flag=True, help='Prints the detail of the response such as protocol, status, and headers.')
def head(url, header, output, verbose):
    '''executes a HTTP HEAD request and prints the response.'''
    client = Client()

    headers = []
    for pair in header:
        headers.append(pair.split(':'))

    client.head(url, verbose, headers, output)

if __name__ == '__main__':
    cli()