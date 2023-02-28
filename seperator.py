import os
import shutil
current_dir = os.getcwd()
openpath = os.path.join(os.getcwd(),'Open_eyes')
closepath = os.path.join(os.getcwd(),'Closed_eyes')
final = os.path.join(current_dir,'mrlEyes_2018_01')
for filename in os.listdir(final):
    if filename.endswith('txt') or filename.endswith('ods'):
        pass
    else:
       innerlist = os.path.join(final,filename)
       print(innerlist)
       files = os.listdir(innerlist)
       for file in files:
        getfile = list(file.split('_'))
        final_file_name = os.path.join(innerlist,file)
        if getfile[4] =='0':
            shutil.copy(final_file_name,closepath)
        else:
            shutil.copy(final_file_name,openpath)

       