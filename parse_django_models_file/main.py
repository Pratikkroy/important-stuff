import sys, os

'''
Conditions to run this code.
1. The models.py file and this file should exist in the same directory.
2. The models dir will be created in the same dir where this file exist.
3. It is assumed that each django model in models.py have inner Meta class.
4. If there is any models directory then this code will overwrite it.
'''

'''
Command to run
python main.py models.py
models.py is the file which contains all the models classes
'''

DIR_NAME = 'models'

def validate_sys_args():
    # check if first sys args is provided
    try:
        input_file = sys.argv[1]
    except Exception as ex:
        print("No argument provided. Please provide the file")
        return False
    
    # check if the given argument is file or not
    if not os.path.isfile(input_file):
        print( input_file + " is not a file")
        return False
    
    return True
    

  
def convert_model_file_to_directory():
    if validate_sys_args():
        create_new_dir(os.path.join(os.getcwd(),DIR_NAME))
        # create init file
        init_file_name = os.path.join(os.path.join(os.getcwd(), DIR_NAME), '__init__.py')
        init_file = open(init_file_name,'w')
        print('New file created:: '+init_file_name)
        input_file = sys.argv[1]
        parse_file(input_file, DIR_NAME, init_file)
    
        
    
def parse_file(input_file, dir_name, init_file):
    try:
        input_file = open(input_file,'r')
    except:
        print('Cannot open file '+ input_file)
        return
    
    file_generator_obj = parse_file_generator(input_file)
    
    # code to get the first line which starts with class
    for line in file_generator_obj:
        if line.strip().startswith('class'):
            break
    
    while True:
        
        try:
            new_file_name = os.path.join(os.path.join(os.getcwd(), dir_name), get_file_name(line)+'.py')
            new_file = open(new_file_name,'w')
        except:
            print('Error in creating new file')
            return
        else:
            print('New file created:: '+new_file_name)
        
        init_file.write('from .'+ new_file_name.split('/')[-1].split('.py')[0] +' import '+get_class_name(line)+'\n')
        new_file.write('from django.db import models\n')
        new_file.write('from . import *\n\n')
        new_file.write(line)
        class_count = 0    # for 'class Meta:' line
        for line in file_generator_obj:
            if line.strip().startswith('class'):
                if class_count == 1: 
                    break
                else:    # for 'class Meta:' line
                    class_count += 1
                    new_file.write(line)
            else:
                new_file.write(line)
                
        # once the input file is done reading it
        # it would call else part
        else:
            new_file.close()
            break      
        new_file.close() 
    
    input_file.close()
    
    

def parse_file_generator(input_file):    
    for line in input_file:
        yield line

def get_file_name(line):
    # example str 'class RolesModel(models.Model):'
    file_name = ''
    count = 0
    for char in get_class_name(line):
        if char.isupper():
            if count == 0:
                count += 1
            else:
                file_name += '_'
        file_name += char
    
    return file_name.lower()       
                
def get_class_name(line):
    # example str 'class RolesModel(models.Model):'
    return line.split('class')[1].strip().split('(')[0].strip()
       
def create_new_file(path, name):
    file = open(path+'/'+name,'w') 
    file.close()
    return file

def create_new_dir(dir_name):
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
        print("New directory created:: "+dir_name)
        
     
        
        
if __name__ == '__main__':
    convert_model_file_to_directory()
    
        