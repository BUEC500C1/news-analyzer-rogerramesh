import os
# import packages
import PyPDF2
import re
path = os.getcwd() 
#print("Current Directory", path)
newpath = "/Users/rogerramesh/GitHub/news-analyzer-rogerramesh/uploads"
os.chdir(newpath)
retval = os.getcwd()
object = PyPDF2.PdfFileReader("sample.pdf")
NumPages = object.getNumPages()
#print(NumPages)
String = "The end"

for i in range(NumPages):
        # Creating a page object
        pageObj = object.getPage(i)
        # Printing Page Number
        print("Page No: ",i)
        # Extracting text from page
        # And splitting it into chunks of lines
        text = pageObj.extractText().split("  ")
        # Finally the lines are stored into list
        # For iterating over list a loop is used
        for i in range(len(text)):
                # Printing the line
                # Lines are seprated using "\n"
                print(text[i],end="\n\n")
        # For Seprating the Pages
        print()



"""
# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    #print("this is page " + str(i)) 
    Text = str(PageObj.extractText())
    f = open("demofile2.txt", "a")
    PageObj = object.getPage(i)
        #print("this is page " + str(i)) 
    Text = str(PageObj.extractText())
    f.write(Text)
    f.write("\n")
    f.close()
    #print(Text)
    #ResSearch = re.search(String, Text)
    #print(ResSearch)
"""

#print(Text)
#print("Current Directory",retval)
#file1 = open("data.txt") 
  
# Reading from file 
#print(file1.read()) 
  
#file1.close() 
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