file = open('C:/Users/Dell/OneDrive/Desktop/filetest.txt','r') 
print(file.read())
print(file.readline())
print(file.readlines())

file = open('C:/Users/Dell/OneDrive/Desktop/filetest.txt','w')
file.write("Rajendar Reddy")

try:
    file = open('C:/Users/Dell/OneDrive/Desktop/filetest.txt','a+')
except Exception as e:
    print(f"Error occured: {e}")
else:
    file.write("\nopening file\nclosing file")
    file.seek(0)
    print(file.read())
    file.close()        


with open('C:/Users/Dell/OneDrive/Desktop/filetest.txt','r') as file:
    print(file.read())



import os
os.mkdir('folder')
os.rmdir('folder')
os.mkdir('parent_folder/child_folder')
os.rmdir('parent_folder')


# create a file inside folder
file_path = os.path.join("foldername","filename")