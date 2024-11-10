import os,shutil
path =r"F:/TestFolder/"
file_path = os.listdir(path)
print(file_path)

folder_type = ["png files","txt files","pdf files","docx files"]

for loop in range(0,4):
    if not os.path.exists(path + folder_type[loop]):
        print(path + folder_type[loop])
        os.makedirs(path + folder_type[loop])
    
for file in file_path:
    if ".png" in file and not os.path.exists(path + "png files/" +file):
        shutil.move(path + file,path + "png files/" +file)
        
    if ".txt" in file and not os.path.exists(path + "txt files/" +file):
        shutil.move(path + file,path + "txt files/" +file)
        
    if ".pdf" in file and not os.path.exists(path + "pdf files/" +file):
        shutil.move(path + file,path + "pdf files/" +file)
        
    if ".docx" in file and not os.path.exists(path + "docx files/" +file):
        shutil.move(path + file,path + "docx files/" +file)

        
    