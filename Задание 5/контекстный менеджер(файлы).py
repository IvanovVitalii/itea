class ContextManagerFile:
    def __init__(self, file, mode, f=0):
        self._file = file
        self._mode = mode
        self._f = f

    def __enter__(self):
        self._f = open(self._file, self._mode)
        return self._f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._f.close()


with ContextManagerFile('test.txt', 'w') as f:
    f.write('!!!')

with ContextManagerFile('test.txt', 'r') as f:
    print(f.read(10))

with open('test.txt', 'r') as f:
    print(f.read(10))