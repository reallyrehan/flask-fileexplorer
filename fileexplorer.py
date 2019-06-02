from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)


@app.route('/<var>', methods=['GET'])
def filePage(var):
    pathC = var.split('>')
    os.chdir('/')
    for i in pathC:
        if i=='':
            continue
        else:
            try:
                os.chdir(i)
            except:
                print(1)
    


    dirList = list(filter(lambda x: os.path.isdir(x), os.listdir('.')))
    fileList = list(filter(lambda x: os.path.isfile(x), os.listdir('.')))


    return render_template('home.html',dirList=dirList,fileList=fileList,currentDir=var)

@app.route('/', methods=['GET'])
def homePage():
    currentDir = '/'
    dirList = os.listdir(currentDir)
    return render_template('home.html',dirList=dirList,currentDir='')


@app.route('/download/<var>')
def downloadFile(var):
    os.chdir('/')

    pathC = var.split('>')
    if(pathC[0]==''):
        pathC.remove(pathC[0])
    
    fPath = '/'.join(pathC)
    fPath='/'+fPath
    fName=pathC[len(pathC)-1]
    #print(fPath)
    return send_file(fPath, attachment_filename=fName)




if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)