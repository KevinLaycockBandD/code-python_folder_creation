#!/usr/bin/python

#example: python create_folders_for_roadmapping_project.py "c:/basefolder"
#example2: python create_folders_for_roadmapping_project.py_2021-04-19 "C:\Users\kevin\Desktop\Workspace\Python\Folder Tool"

import sys, os, argparse, uuid, csv, locale, getpass
from datetime import datetime
from pathlib import Path

def main(args):
        

        print("")
        print("------------------------------")
        print(" Results:")

        # Parent Directory path
        # todo - read from the parameter basepath which is submitted from the command line
        # https://stackoverflow.com/questions/14360389/getting-file-path-from-command-line-argument-in-python/47324233

        # parser = argparse.ArgumentParser()
        # parser.add_argument("file_path", type=Path)

        # p = parser.parse_args()
        # print(p.file_path, type(p.file_path), p.file_path.exists())


        # you could just have it run the "current" folder.
        #parent_dir = "C:\\projects\\ad-hoc\\ouput"

      

        # TODO allow for manual input of client name, project name and project code?
        #print('Enter client name:')
        #clientName = input()
        #print('Hello, ' + clientName)

        # print('Enter project name:')
        # projectName = input()
        # print('Project Name: ' + projectName)

        # print('Enter project code:')
        # projectCode = input()
        # print('Project Name: ' + projectCode)

        # print('Enter project year:')
        # projectYear= input()
        # print('Project year: ' + projectYear)

        #Manual folder creation
        clientName = "Carleton"
        projectName = "Carleton CAP 2.0"
        projectCode = "15470"
        projectDate = "2021"
        bdInternal =  "B&D Internal"
        projectFolder = projectDate + ' ' + projectName + ' (' + projectCode + ')'
        
        # print("")
        # print("------------------------------")
        # print ('project folder: ', projectFolder)

        # Sub Folders are:
        # 01 project management
        # 02 doc and data
        # 03 visioning
        # 04 initiatives
        # 05 model & tech roadmap
        # 06 delivery roadmap


        # set as a "list" and iterate over that list

        # TODO - check to see if the folder already exists.. if so, skip it & print that out.
        os.path.isdir

        #create path to ...Box\Client for current user. e.g C:\Users\kevin\Box\Clients
        #basepath passed in command line would just be "C:/Users/"
        #get user name to build correct path
        # import getpass
        # user = getpass.getuser()
        # print ('User is: ', user)
        # print("")
        # print("------------------------------")

        # #parent_dir_alt = os.path.join(user, "/Box/Clients/")
        # parent_dir_alt = os.path.join(user, "/Desktop/Workspace/Python/Folder Tool")
        # print('Alternative parent directory method: ', parent_dir_alt)
        # print("")
        # print("------------------------------")


        parent_dir = "C:/Users/kevin/Box/Clients/South, The University of the/B&D Internal/2021 Climate Action Planning (10081)/B&D Project Documents"
        # clientDirectory = os.path.join(parent_dir,clientName)
        # os.mkdir(clientDirectory)
        # print ('Client Directory: ', clientDirectory)

        # internal = os.path.join(clientDirectory,bdInternal)
        # os.mkdir(internal)
        # print ('BD Internal Directory: ', internal)

        # folder = os.path.join(internal,projectFolder)
        # os.mkdir(folder)
        # print ('Project folder: ', folder )

  # TODO: make this into a loop
        #subDirectory = os.path.join(directory,subFolder1)

        subFolders = set()
        subFolders.add("01 project management")
        subFolders.add("02 doc and data")
        subFolders.add("03 visioning")
        subFolders.add("04 initiatives")
        subFolders.add("05 model & tech roadmap")
        subFolders.add("06 delivery roadmap")

        for sf in subFolders:
                print(sf)

                path = os.path.join(parent_dir, sf)

                print("------------------------------")
                print("Creating sf: "+ path)
                os.mkdir(path)
                print('Sub-folders ',path + "  - created!")


        print("------------------------------")
        print("")
              
               
        
        print("")
        print("______________________________")
        

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Creates folders for a new Roadmapping project')
        parser.add_argument('basepath', help='path where you want to make folders')
        args = parser.parse_args()
        main(args)



