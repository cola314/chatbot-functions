import os
import importlib

test_py_path = os.path.dirname(__file__)

def is_function_folder(folder):
    return folder not in ['.github', 'build', 'template', '.git']

folders = []
with os.scandir(test_py_path) as entires:
    for entry in entires:
        if entry.is_dir() and is_function_folder(entry.name):
            folders.append(entry.name)

total_tests = 0
for folder in folders:
    module = importlib.import_module(folder + ".handler_test")
    module.test_handle()
    total_tests += 1

print(str(total_tests) + " test success")