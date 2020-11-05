import zipfile
import os
import shutil

os.mkdir('answer')
os.mkdir('archive')
my_dir=os.getcwd()+'\\answer'
my_zip=os.getcwd()+'\\main.zip'
my_archive=os.getcwd()+'\\archive'

with zipfile.ZipFile(my_zip) as zip_file:
    zip_file.extractall(my_archive)

for current_dir, dirs, files in os.walk(my_archive):
    for file in files:
        if '.py' in file:
            my_dir_file=my_dir+'\\'+os.path.basename(file)
            shutil.copy(os.path.join(current_dir, file),my_dir_file)
shutil.rmtree(my_archive)