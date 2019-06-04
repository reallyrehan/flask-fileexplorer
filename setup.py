from flask import Flask, render_template, request, send_file, redirect
import os

app = Flask(__name__)

try:
    f= open('hidden.txt','r')
    fileText=f.read()
    fileText = fileText.split('\n')
except:
    fileText=[]

hiddenList = []
for i in fileText:
    hiddenList.append(i)
f.close()


try:
    f= open('favorites.txt','r')
    fileText=f.read()
    fileText = fileText.split('\n')
except:
    fileText=[]

favList = []
for i in fileText:
    favList.append(i.replace('/','>'))
f.close()
if(len(favList)>3):
    favList=favList[0:3]








def hidden(path):
    for i in hiddenList:
        if i in path:
            return True
    
    return False



def changeDirectory(path):
    pathC = path.split('>')
    os.chdir('/')

    if(pathC[0]==""):
        pathC.remove(pathC[0])
    
    myPath = '/'.join(pathC)
    try:
        os.chdir(myPath)
        return True
    except:
        return False
    
def getDirList():


    dList= list(filter(lambda x: os.path.isdir(x), os.listdir('.')))
    finalList = []
    curDir=os.getcwd()

    for i in dList:
        if(hidden(curDir+'/'+i)==False):
            finalList.append(i)

    return(finalList)


def getFileList():

    dList = list(filter(lambda x: os.path.isfile(x), os.listdir('.')))

    finalList = []
    curDir=os.getcwd()

    for i in dList:
        if(hidden(curDir+'/'+i)==False):
            finalList.append(i)

    return(finalList)






@app.route('/<var>', methods=['GET'])
def filePage(var):
    
    if(changeDirectory(var)==False):
        #Invalid Directory
        print("Directory Doesn't Exist")
        return redirect("/", code=302)

     
    dirList = getDirList()
    fileList = getFileList()


    return render_template('home.html',dirList=dirList,fileList=fileList,currentDir=var,favList=favList)

@app.route('/', methods=['GET'])
def homePage():
    os.chdir('/')
    dirList = getDirList()
    fileList=getFileList()
    return render_template('home.html',dirList=dirList,fileList=fileList,currentDir='/',favList=favList)


@app.route('/download/<var>')
def downloadFile(var):
    os.chdir('/')

    pathC = var.split('>')
    if(pathC[0]==''):
        pathC.remove(pathC[0])
    
    fPath = '/'.join(pathC)
    fPath='/'+fPath
    if(hidden(fPath)):
        #FILE HIDDEN
        return redirect("/", code=100)


    fName=pathC[len(pathC)-1]
    #print(fPath)
    return send_file(fPath, attachment_filename=fName)




if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)