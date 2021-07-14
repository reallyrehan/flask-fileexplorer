from flask import Flask, render_template, request, send_file, redirect, session,jsonify
import os
import sys
import json
from flask_fontawesome import FontAwesome
import zipfile
from werkzeug.utils import secure_filename
from hurry.filesize import size
from datetime import datetime
import filetype


from urllib.parse import unquote
import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is: " + hostname)    
print("Your Computer IP Address is: " + IPAddr)   
maxNameLength = 15


app = Flask(__name__)

#FoNT AWESOME
fa = FontAwesome(app)


app.secret_key = 'my_secret_key'

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
hiddenList = data["Hidden"]
favList = data["Favorites"]
password = data["Password"]



currentDirectory=data["rootDir"]

osWindows = False #Not Windows

default_view = 0

tp_dict = {'image':'photo-icon.png','audio':'audio-icon.png','video':'video-icon.png'}

# if 'win' in sys.platform:
#     # import win32api
#     osWindows = True
#     #WINDOWS FEATURE
#     drives = win32api.GetLogicalDriveStrings()
#     drives=drives.replace('\\','')
#     drives = drives.split('\000')[:-1]
#     drives.extend(favList)
#     favList=drives



if(len(favList)>3):
    favList=favList[0:3]
    
print(favList)
# if(len(favList)>0):
#     for i in range(0,len(favList)):
        
#         favList[i]=favList[i].replace('\\','>') #CHANGE FOR MAC




#WINDOWS FEATURE
# drives = win32api.GetLogicalDriveStrings()
# drives=drives.replace('\\','')
# drives = drives.split('\000')[:-1]
# drives.extend(favList)
# favList=drives











def make_zipfile(output_filename, source_dir):
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)




@app.route('/login/')
def loginMethod():
    global password
    if(password==''):
        session['login'] = True


    if('login' in session):
        return redirect('/')
    else:
        return render_template('login.html')


@app.route('/login/', methods=['POST'])
def loginPost():
    global password

    text = request.form['text']
    if(text==password):
        session['login'] = True

        return redirect('/')
    else:
        return redirect('/login/')

@app.route('/logout/')
def logoutMethod():
    if('login' in session):
        session.pop('login',None)
    return redirect('/login/')
    
#@app.route('/exit/')
#def exitMethod():
#    exit()




def hidden(path):

    for i in hiddenList:
        if i != '' and i in path:
            return True
    
    return False



def changeDirectory(path):
    global currentDirectory, osWindows


    pathC = path.split('/')
    # print(path)

    
    if(osWindows):
        myPath = '//'.join(pathC)+'//'
    else:
        myPath = '/'+'/'.join(pathC)

    # print(myPath)
    myPath = unquote(myPath)

    try:
        os.chdir(myPath)
        ans=True
        if(currentDirectory not in os.getcwd()):
            ans = False
    except:
        ans=False
    
    

    return ans
    
# def getDirList():


#     dList= list(filter(lambda x: os.path.isdir(x), os.listdir('.')))
#     finalList = []
#     curDir=os.getcwd()

#     for i in dList:
#         if(hidden(curDir+'/'+i)==False):
#             finalList.append(i)

#     return(finalList)

@app.route('/changeView')
def changeView():
    global default_view

    # print('view received')

    v = int(request.args.get('view', 0))

    if v in [0,1]:
        default_view = v
    else:
        default_view = 0


    return jsonify({
 
        "txt":default_view,
     
    })



def getDirList(view,visibility):
    # print(default_view)

    global maxNameLength,tp_dict
    
    if view == 0:
        dText = '<div id ="view0_container" class = "container" __DISPLAY__  ><div class = "row mt-4"><h5></h5></div> <hr><div class = "row mt-4">'


        dText_original = """
            <div class="col-md-2 col-sm-4 col-6 mt-2">
            <div class="thumbnail hvr-shadow">

                <a href="/files/{{currentDir}}/{{f_url}}"><img src = '/static/{{image}}' class='img-thumbnail' style="border:0px;"/><p style="color:black; text-align:center; text-decoration:none;">
                        <p style="color:black;" data-toggle="tooltip" data-placement="right" title="{{f_complete}}">
    {{f}}
    </p>
                </p></a>
                
            </div>
            </div>
        """

    elif view == 1:
        dText = """



<div id ="view1_container" class = "container" __DISPLAY__ >
        <div class = "row mt-4">
            <div class="col-3 mb-2" style=" text-align:center;" ><b>Name</b></div>
            <div class="col-3" style=" text-align:center;" ><b>Created Time</b></div>
            <div class="col-3" style=" text-align:center;"><b>Modified Time</b></div>
            <div class="col-3" style=" text-align:center;"><b>Size</b></div>
</div>
<hr>
<div class = "row">
        """
        dText_original = """
       



            <div class="col-3" style="margin-bottom:-10px">

                <a href="/files/{{currentDir}}/{{f_url}}">
                
                <img src = '/static/{{image}}'  style="position:absolute; height:25px; width:25px; border:0px;"/>

                <p style="margin-left:35px; color:black; text-align:left; text-decoration:none;">
    {{f}}</p>
                </a>
                
            </div>
            <div class="col-3" style="margin-bottom:-10px"><p style="margin-left:45px;">{{dtc}}</p></div>
            <div class="col-3" style="margin-bottom:-10px"><p style="margin-left:45px;">{{dtm}}</p></div>
            <div class="col-3" style="margin-bottom:-10px; "><p style="margin-left:110px;">{{size}}</p></div>

        """



    if visibility:
        dText = dText.replace('__DISPLAY__','style="display:none;"')
    else:
        dText = dText.replace('__DISPLAY__','')







    dList = list(os.listdir('.'))

    dList= list(filter(lambda x: os.path.isdir(x), os.listdir('.')))
    fList = list(filter(lambda x: not os.path.isdir(x), os.listdir('.')))




    curDir=os.getcwd()
    # print(os.stat(os.getcwd()))


    for i in dList:
        if(hidden(curDir+'/'+i)==False):
            image = 'folder5.png'
            if view == 0:
                if len(i)>maxNameLength:
                    dots = "..."
                else:
                    dots = ""

                dt = dText_original.replace("{{f}}",i[0:maxNameLength]+dots).replace("{{f_url}}",i).replace('{{currentDir}}',curDir).replace('{{f_complete}}',i).replace('{{image}}',image)
                dText += dt[:]
            elif view == 1:
                try:
                    dir_stats = os.stat(i)
                    dt = dText_original.replace("{{f}}",i).replace("{{f_url}}",i).replace('{{currentDir}}',curDir).replace('{{f_complete}}',i).replace("{{dtc}}",datetime.utcfromtimestamp(dir_stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')).replace("{{dtm}}",datetime.utcfromtimestamp(dir_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')).replace("{{size}}","---").replace('{{image}}',image)
                    dText += dt[:]
                except:
                    pass

    dText+='</div><div class = "row mt-4"><h5></h5></div> <hr><div class = "row mt-4">'
    
    # </div><hr><div class = "row">'




    for i in fList:
        if(hidden(curDir+'/'+i)==False):
            image = None
            try:
                kind = filetype.guess(i)

                if kind:
                    tp = kind.mime.split('/')[0]

                    if tp in tp_dict:
                        image = tp_dict[tp]

            except:
                pass

            if not image:
                image = 'file-test2.png'
            
            if view == 0:
                if len(i)>maxNameLength:
                    dots = "..."
                else:
                    dots = ""
                    
                dt = dText_original.replace("{{f}}",i[0:maxNameLength]+dots).replace("{{f_url}}",i).replace('{{currentDir}}',curDir).replace('{{f_complete}}',i).replace('{{image}}',image).replace('/files/','/download/')
                dText += dt[:]
            elif view == 1:
                try:
                    dir_stats = os.stat(i)
                    dt = dText_original.replace("{{f}}",i).replace("{{f_url}}",i).replace('{{currentDir}}',curDir).replace('{{f_complete}}',i).replace("{{dtc}}",datetime.utcfromtimestamp(dir_stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')).replace("{{dtm}}",datetime.utcfromtimestamp(dir_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')).replace("{{size}}",size(dir_stats.st_size)).replace('{{image}}',image).replace('/files/','/download/')
                    dText += dt[:]
                except:
                    pass


    dText+= "</div></div>"
    return dText











def getFileList():

    dList = list(filter(lambda x: os.path.isfile(x), os.listdir('.')))

    finalList = []
    curDir=os.getcwd()

    for i in dList:
        if(hidden(curDir+'/'+i)==False):
            finalList.append(i)

    return(finalList)






@app.route('/files/<path:var>', methods=['GET'])
def filePage(var):
    global default_view


    if('login' not in session):
        return redirect('/login/')


    if(changeDirectory(var)==False):
        #Invalid Directory
        print("Directory Doesn't Exist")
        return render_template('404.html',errorCode=300,errorText='Invalid Directory Path',favList=favList)
     


    try:
        if default_view == 1:
            dirList_1 = getDirList(0,True)
            dirList_2 = getDirList(1,False)
            var1,var2 = "","DISABLED"
        else:
            dirList_1 = getDirList(1,True)
            dirList_2 = getDirList(0,False)
            var1,var2 = "DISABLED",""

        dirList = dirList_1+dirList_2
        # fileList = getFileList()
    except:
        return render_template('404.html',errorCode=200,errorText='Permission Denied',favList=favList)
    
    return render_template('home.html',dirList=dirList,currentDir=var,favList=favList,view0_button=var1,view1_button = var2)


@app.route('/files/', methods=['GET'])
def filePageRoot():
    global default_view


    var = ""

    if('login' not in session):
        return redirect('/login/')


    if(changeDirectory(var)==False):
        #Invalid Directory
        print("Directory Doesn't Exist")
        return render_template('404.html',errorCode=300,errorText='Invalid Directory Path',favList=favList)
    
    
    if default_view == 1:
        dirList_1 = getDirList(0,True)
        dirList_2 = getDirList(1,False)
        var1,var2 = "","DISABLED"
    else:
        dirList_1 = getDirList(1,True)
        dirList_2 = getDirList(0,False)
        var1,var2 = "DISABLED",""

    dirList = dirList_1+dirList_2
    try:
        pass
        # fileList = getFileList()
    except:
        return render_template('404.html',errorCode=200,errorText='Permission Denied',favList=favList)

    return render_template('home.html',dirList=dirList,currentDir=var,favList=favList,view0_button=var1,view1_button = var2)


@app.route('/', methods=['GET'])
def homePage():

    global currentDirectory, osWindows

    if('login' not in session):
        return redirect('/login/')
    
    if osWindows:
        if(currentDirectory == ""):
            return redirect('/C:')
        else:
            # cura = currentDirectory

            cura='>'.join(currentDirectory.split('\\'))
            return redirect('/'+cura)
    else:
        return redirect('/files/')
        
        #REDIRECT TO UNTITLED OR C DRIVE FOR WINDOWS OR / FOR MAC



@app.route('/download/<path:var>')
def downloadFile(var):

    if('login' not in session):
        return redirect('/login/')
    
    #os.chdir(currentDirectory)

    
    pathC = unquote(var).split('/')
    if(pathC[0]==''):
        pathC.remove(pathC[0])
    
    fPath = '/'+currentDirectory+'//'.join(pathC)

    
    
    if(hidden(fPath)):
        #FILE HIDDEN
        return render_template('404.html',errorCode=100,errorText='File Hidden',favList=favList)


    fName=pathC[len(pathC)-1]
    #print(fPath)
    return send_file(fPath, attachment_filename=fName)
    try:
        return send_file(fPath, attachment_filename=fName)
    except:
        return render_template('404.html',errorCode=200,errorText='Permission Denied',favList=favList)



@app.route('/downloadFolder/<path:var>')
def downloadFolder(var):

    if('login' not in session):
        return redirect('/login/')
    
    #os.chdir(currentDirectory)

    pathC = var.split('/')
    if(pathC[0]==''):
        pathC.remove(pathC[0])
    
    fPath = '/'+currentDirectory+'//'.join(pathC)
    
    
    if(hidden(fPath)):
        #FILE HIDDEN
        return render_template('404.html',errorCode=100,errorText='File Hidden',favList=favList)


    fName=pathC[len(pathC)-1]+'.zip'
    
    try:
        make_zipfile('C:\\Users\\reall\\Downloads\\temp\\abc.zip',os.getcwd())
        return send_file('C:\\Users\\reall\\Downloads\\temp\\abc.zip', attachment_filename=fName)
    except:
        return render_template('404.html',errorCode=200,errorText='Permission Denied',favList=favList)


@app.errorhandler(404)
def page_not_found(e):
    if('login' not in session):
        return redirect('/login/')
    
    # note that we set the 404 status explicitly
    return render_template('404.html',errorCode=404,errorText='Page Not Found',favList=favList), 404



@app.route('/upload/<path:var>', methods = ['GET', 'POST'])
def uploadFile(var):

    if('login' not in session):
    
        return render_template('login.html')

    text = ""
    if request.method == 'POST':
        pathC = var.split('/')

        if(pathC[0]==''):
            pathC.remove(pathC[0])
        
        fPath = '/'+currentDirectory+'//'.join(pathC)
    
    
        if(hidden(fPath)):
            #FILE HIDDEN
            return render_template('404.html',errorCode=100,errorText='File Hidden',favList=favList)


        files = request.files.getlist('files[]') 
        fileNo=0
        for file in files:
            fupload = os.path.join(fPath,file.filename)

            if secure_filename(file.filename) and not os.path.exists(fupload):
                try:
                    file.save(fupload)    
                    print(file.filename + ' Uploaded')
                    text = text + file.filename + ' Uploaded<br>'
 
                    fileNo = fileNo +1
                except Exception as e:
                    print(file.filename + ' Failed with Exception '+str(e))
                    text = text + file.filename + ' Failed with Exception '+str(e) + '<br>'

                    continue
            else:
                print(file.filename + ' Failed because File Already Exists or File Type Issue')
                text = text + file.filename + ' Failed because File Already Exists or File Type not secure <br>'

            
          
    fileNo2 = len(files)-fileNo
    return render_template('uploadsuccess.html',text=text,fileNo=fileNo,fileNo2=fileNo2,favList=favList)
        




if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)