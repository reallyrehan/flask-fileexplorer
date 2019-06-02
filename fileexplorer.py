from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/<var>', methods=['GET'])
def filePage(var):
    pathC = var.split('-')
    os.chdir('/')

    for i in pathC:
        if i=='':
            continue
        else:
            os.chdir(i)
    
    




    dirList = os.listdir()





    return render_template('home.html',dirList=dirList,currentDir=var)

@app.route('/', methods=['GET'])
def homePage():
    currentDir = '/'
    dirList = os.listdir(currentDir)
    return render_template('home.html',dirList=dirList,currentDir='')

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)