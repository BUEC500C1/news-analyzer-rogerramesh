"""
User stories
Create a DB that can store the files that being uploaded.
Set a max file size threshold that cannot be exceeded
API should be able to browse through local files on computer
"""
# Browse files on local computer
def browse():
    """
    Checks local computer to see directories and what files are available
    returns whether or not file size is too large
    returns whether or not file size is incompatible
    """
    
    
#establish connection to DB
def connect():
    """
    Connects to DB hosted on Server
    returns whether or not it can connect to databases
    """
    
#method to file upload Python script
def sendtoDB():
    """
    retrieves file held on browse() method and sends it directly to a database
    returns whether or not it is a successful upload
    """

