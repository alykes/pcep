# Started but still needs work, moving on so that I can progress through the course, will come back to this lab!
# !!!NOT FINISHED!!!
# !!!NOT FINISHED!!!
# !!!NOT FINISHED!!!
# https://github.com/adamo78/Python_PCAP_Learning_Exercises_Edube/blob/main/4.4.1.8%20The%20os%20module:%20LAB

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


############################
import os

def find_dir(dir_list, name):
    for dir in dir_list:
        if os.path.isdir(dir):
            if name in dir:
                return dir
            else:
                subdir_list = [os.path.join(dir, sub_dir) for sub_dir in os.listdir(dir)]
                subdir_list += [sub_dir for sub_dir in os.listdir(dir) if os.path.isdir(sub_dir)]
                python_dir = find_dir(subdir_list, name)
                if python_dir:
                    return python_dir
    return None

dir_list = ['/usr/local', '/usr/bin', '/usr/share']
name = 'python'
result = find_dir(dir_list, name)
print(result)
