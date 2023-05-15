# Started but still needs work, moving on so that I can progress through the course, will come back to this lab!
# !!!NOT FINISHED!!!
# !!!NOT FINISHED!!!
# !!!NOT FINISHED!!!

import os

def find(path, dir):

    path = get_abs_path(path)

    print(paths)

    for content in os.listdir(path):
        if os.path.isdir(content):
            print(os.getcwd() + "/" + content + " is a path!")
            paths.append(path + content)
        # Add elif os.path contains `dir` then add it to an array of found_paths!!
        else:
            print(content, "is not a no dir")
            
    print(paths)

def get_abs_path(path):
    # Find the absolute path of where to start the search from
    # Remove trailing /
    if path[-1] == '/':
        path = path[0:-1]
    
    # path is where the search should start
    if path[0:2] == "..":
        os.chdir('../')
        path = os.getcwd() + path[2:]
        paths.append(path)
    elif path [0] == ".":
        path = os.getcwd() + "/" + path[1:]
        paths.append(path)
    else:
        paths.append(path)

    return path

# Add a function to change into each of the array element lists and search for the `dir`

paths = []

os.mkdir('one')
find('./', 'one')


