from flask import Flask, render_template, request, send_file, redirect
import os
import sys

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

currentDirectory='/'
currentDirectory='/Users/rehan/Documents'




def hidden(path):
    for i in hiddenList:
        if i in path:
            return True
    
    return False



def changeDirectory(path):
    global currentDirectory

    pathC = path.split('>')
    
    os.chdir(currentDirectory)
    if(pathC[0]==""):
        pathC.remove(pathC[0])
    
    myPath = '/'.join(pathC)
    try:
        os.chdir(myPath)
        ans=True
        if(currentDirectory not in os.getcwd()):
            ans = False
    except:
        ans=False
    
    

    return ans
    
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
    global currentDirectory
    os.chdir(currentDirectory)
    dirList = getDirList()
    fileList=getFileList()
    return render_template('home.html',dirList=dirList,fileList=fileList,currentDir="",favList=favList)


@app.route('/download/<var>')
def downloadFile(var):
    global currentDirectory
    os.chdir(currentDirectory)

    pathC = var.split('>')
    if(pathC[0]==''):
        pathC.remove(pathC[0])
    
    fPath = '/'.join(pathC)
    fPath=currentDirectory+fPath
    
    if(hidden(fPath) or currentDirectory not in fPath):
        #FILE HIDDEN
        return redirect("/", code=100)


    fName=pathC[len(pathC)-1]
    #print(fPath)
    try:
        return send_file(fPath, attachment_filename=fName)
    except:
        return redirect("PERMISSION DENIED", code=200)




if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)