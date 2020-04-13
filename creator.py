#!/usr/bin/python3

from sys import argv,exit
from os import chdir,mkdir,getcwd,system
import getopt


def usage():

    print("Usage: {} [OPTIONS] DIR".format(argv[0]))
    print()
    print("OPTIONS:")
    print("   -h  --help  help manual")
    print("   -v  --env   create a virtualenv")
    exit(-1);



def main():

    try:
        options, args = getopt.getopt(argv[1:], 'hv', ['help', 'env'])

    except getopt.GetoptError as err:
        print(error)
        usage()

    VENV_FLAG = 0
    
    for opt, a in options:
        if opt in ['-h','--help']:
            usage()
            exit(2)
        elif opt in ['-v','--env']:
            print("the -v work men")
            VENV_FLAG =  1


            
    if not args:
        usage()

    #making a directory and go to it
    mkdir(args[0])
    path = getcwd()
    chdir(path +'/' + args[0])

    if VENV_FLAG:
        system('virtualenv {}'.format("venv"))



    #initialize a git repo
    system('git init')
   
    liste_files = ['.gitignore', 'Readme']

    #create a file for each filename in the liste
    for fichier in liste_files:
        with open(fichier,'w+') as f:
            if fichier == '.gitignore':
                f.write("venv")
            if fichier == 'Readme':
                f.write('this is a readme file for this project')


if __name__ == '__main__':
    main()
