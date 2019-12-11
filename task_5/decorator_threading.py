from threading import Thread
import urllib.request

list_http = [
'https://www.python.org/static/img/python-logo.png',
'https://www.python.org/static/img/python-logo.png',
'https://www.python.org/static/img/python-logo.png',
'https://st2.depositphotos.com/2001755/5408/i/950/depositphotos_54081723-stock-photo-beautiful-nature-landscape.jpg',
'https://www.python.org/static/img/python-logo.png',
'https://www.python.org/static/img/python-logo.png',
'https://www.python.org/static/img/python-logo.png',
'https://www.python.org/static/img/python-logo.png',
'https://www.python.org/static/img/python-logo.png',
'https://www.python.org/static/img/python-logo.png'
]

list_name_thread = [n for n in range(len(list_http))]


def decorator(name, daemon):
    def decor(func):
        def wrapper(*args, **kwargs):
            result = []
            for i in list_http:
                t = Thread(target=func, args=(i, "a"), kwargs=kwargs, name=name + str(i), daemon=daemon)
                result.append(t.start())
                print(t.getName())
                print(t.isDaemon())
            return result
        return wrapper
    return decor


@decorator('Thread-', True)
def download(http, name):
    urllib.request.urlretrieve(http, f'{name}.png')


download()
