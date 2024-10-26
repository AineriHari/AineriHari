# class Open_file:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()


# with Open_file("a.txt", 'r') as f:
#     print(f.read())

# print(f.closed)

# class reader:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
    
#     def __iter__(self):
#         self.f = open(self.filename, self.mode)
#         for data in self.f:
#             yield self.f.readline()
#         self.f.close()


# for data in reader("a.txt", 'r'):
#     print(data, end="")

import os
from contextlib import contextmanager


# @contextmanager
# def open_file(filename, mode):
#     f = open(filename, mode)
#     yield f
#     f.close()

# with open_file('a.txt', 'r') as f:
#     print(f.read())

# print(f.closed)

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('venv'):
    print(os.listdir())
