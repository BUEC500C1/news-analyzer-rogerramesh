import os
path = os.getcwd() 
print("Current Directory", path)
newpath = "/Users/rogerramesh/GitHub/news-analyzer-rogerramesh/uploads"
os.chdir(newpath)
retval = os.getcwd()

print("Current Directory",retval)
file1 = open("data.txt") 
  
# Reading from file 
print(file1.read()) 
  
file1.close() 
# prints parent directory 
# List all files in a directory using os.listdir
"""
basepath = 'uploads/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)
"""
"""
with open('data.txt', 'r') as f:
    data = f.read()
"""