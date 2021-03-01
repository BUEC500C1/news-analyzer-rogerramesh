import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import PyPDF2
from datetime import datetime

now = datetime.now()

app=Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)


@app.route('/parse', methods=['POST']) 
def parse_doc():

    path = os.getcwd() 
    print("Current Directory", path)
    newpath = "/Users/rogerramesh/GitHub/news-analyzer-rogerramesh/uploads"
    os.chdir(newpath)
    retval = os.getcwd()
    object = PyPDF2.PdfFileReader("sample.pdf")

    NumPages = object.getNumPages()
    
#print(NumPages)
    String = "The end"


    counter=0
# extract text and do the search
    for i in range(0, NumPages):
        counter = counter+1
        PageObj = object.getPage(i)
        #print("this is page " + str(i)) 
        Text = str(PageObj.extractText())
        res = "demo" + "file" + str(counter) + ".txt"
        f = open(res, "a")
        PageObj = object.getPage(i)
        
            #print("this is page " + str(i)) 
        Text = str(PageObj.extractText())
        f.write("Page " +str(i) + Text)
        f.write("\n")
        f.close()
      
    
    #print("Current Directory",retval)
    #file1 = open("data.txt") 
  
    # Reading from file 
    #print(file1.read())
    return render_template('result.html')

if __name__ == "__main__":
    app.run(host = '127.0.0.1',port = 5000, debug = False)