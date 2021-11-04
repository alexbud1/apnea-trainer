import matplotlib.pyplot as plt
import numpy as np
import os


def draw_apnea(time):
    x = []
    y = []
    ######getting data
    f = open("base.txt", "a")
    f.write("\n")
    f.write(str(time))
    f.close()
    f = open("base.txt", "r")
    input_string = f.read()
    f.close()

    user_list = input_string.split()
########

    # convert each item to int type
    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = float(user_list[i])
        x.append(i+1)
    
    ##### illustration creation
    y = user_list
    plt.yticks(np.arange(0, 6, step=1.0))
    plt.xticks(np.arange(1,len(x)+1,step = 1))
    plt.bar(x,y)
    plt.title("Apnea Progress")
    plt.xlabel("Attempts")
    plt.ylabel("Apnea time")
    plt.grid(axis = 'y')

    plt.savefig('plot.png', dpi=300, bbox_inches='tight')
    plt.clf()

def delete_graphic():
    os.remove('plot.png')
    print("deleted")


# def delete_infographic():
#     os.remove('ploti.png')

def clear_file():
    open("base.txt", 'w').close()

def delete_last_string():
   with open(r"base.txt", 'r+') as fp:
    # read an store all lines into list
    lines = fp.readlines()
    # move file pointer to the beginning of a file
    fp.seek(0)
    # truncate the file
    fp.truncate()

    # start writing lines except the last line
    # lines[:-1] from line 0 to the second last line
    fp.writelines(lines[:-1])

def check_progress():
    x = []
    y = []

    f = open("base.txt", "r")
    input_string = f.read()
    f.close()
    print(input_string)

    user_list = input_string.split()
    #print('list: ', user_list)
########
    # convert each item to int type
    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = float(user_list[i])
        x.append(i+1)
    
    ##### illustration creation
    y = user_list
    plt.yticks(np.arange(0, 6, step=1.0))
    plt.xticks(np.arange(1,len(x)+1,step = 1))
    plt.bar(x,y)
    plt.title("Apnea Progress")
    plt.xlabel("Attempts")
    plt.ylabel("Apnea time")
    plt.grid(axis = 'y')
    plt.savefig('plot.png', dpi=300, bbox_inches='tight')
    plt.clf()

def draw_cwf(depth):
    x = []
    y = []
    ######getting data
    f = open("cwf.txt", "a")
    f.write("\n")
    f.write(str(depth))
    f.close()
    f = open("cwf.txt", "r")
    input_string = f.read()
    f.close()

    user_list = input_string.split()
########

    # convert each item to int type
    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = float(user_list[i])
        x.append(i+1)
    
    ##### illustration creation
    y = user_list
    plt.yticks(np.arange(0, 35, step=1.0))
    plt.xticks(np.arange(1,len(x)+1,step = 1))
    plt.bar(x,y)
    plt.title("Freediving Progress")
    plt.xlabel("Attempts")
    plt.ylabel("Freediving depth")
    plt.grid(axis = 'y')

    plt.savefig('cwf.png', dpi=300, bbox_inches='tight')
    plt.clf()

def delete_cwf():
    os.remove('cwf.png')
    print("deleted")

def clear_cwf():
    open("cwf.txt", 'w').close()

def delete_last_string_cwf():
   with open(r"cwf.txt", 'r+') as fp:
    # read an store all lines into list
    lines = fp.readlines()
    # move file pointer to the beginning of a file
    fp.seek(0)
    # truncate the file
    fp.truncate()

    # start writing lines except the last line
    # lines[:-1] from line 0 to the second last line
    fp.writelines(lines[:-1])

def check_progress_cwf():
    x = []
    y = []

    f = open("cwf.txt", "r")
    input_string = f.read()
    f.close()
    print(input_string)

    user_list = input_string.split()
    #print('list: ', user_list)
########
    # convert each item to int type
    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = float(user_list[i])
        x.append(i+1)
    
    ##### illustration creation
    y = user_list
    plt.yticks(np.arange(0, 35, step=1.0))
    plt.xticks(np.arange(1,len(x)+1,step = 1))
    plt.bar(x,y)
    plt.title("Freediving Progress")
    plt.xlabel("Attempts")
    plt.ylabel("Freediving depth")
    plt.grid(axis = 'y')
    plt.savefig('cwf.png', dpi=300, bbox_inches='tight')
    plt.clf()