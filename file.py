import os
import shutil
soruce = "C:/Users/Bhavesh Sakthivel/Downloads/Photos"
destination ="C:/Users/Bhavesh Sakthivel/OneDrive/Desktop/Images"
list_of_files = os.listdir(soruce)
#print(list_of_files)
for filename in list_of_files:
    name,extension=os.path.splitext(filename)
    #print(name)
    #print(extension)
    if extension == " ":
        continue
    if extension in[".png","jpeg","jpg"]:
        path1=soruce+'/'+filename
        path2=destination+'/'+"image files"
        path3=destination+'/'+"image files"+'/'+filename
        if os.path.exists(path2): 
            print("Moving " + filename + ".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + filename + ".....") 
            shutil.move(path1, path3)