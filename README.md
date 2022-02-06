# WiFile # 

A file explorer that works over local area network (Wi-Fi/Ethernet) using Flask server. You can explore a computer's complete directory and download any file. Moreover, it also lets you stream videos or audio files if your browser supports it.

**New Features** 🎉
-
- Significant performance improvements - incorporated jinja for dynamic output generation 🔥
- Added QR Code Sharing - share files using QR codes 📲
- Folder Breadcrumbs - easily navigate back and forth between folders 🍞

**Description**
-
Server works on,
- Windows 
- Mac
- Linux [(Tested on Ubuntu 18.04)](https://github.com/reallyrehan/flask-fileexplorer/issues/7)

It is written in Python and tested it on Mac and Windows.

**Frameworks**
-
- Flask (Server)
- Bootstrap 4 

Flask has been used to run the server and serve up the html pages. Meanwhile, Bootstrap has been used to show the Folders and the Files. To open any folder, just click on it and to download/stream any file, just click on it.

**Snapshots**
-

**Grid Mode**
![Demo](static/demo_1.png)

**List Mode**
![Demo](static/demo_2.png)


**How to Run**
-
Clone this repository by using,
    
    git clone https://github.com/reallyrehan/flask-fileexplorer.git

Make sure you have flask installed. You can use the following command to install flask,

    pip install -r requirements.txt
    
Now, open terminal/command prompt in the flask-fileexplorer directory and run the setup.py file by using the following command,

    python setup.py

You will have to configure the [config.json](config.json) file with your paths,

Example for Mac,

    "Favorites":    ["Users/rehanahmed/Downloads","Users/rehanahmed/Documents"],

Example for Windows,

    "Favorites":    ["C://Users//Administrator//Documents","C://Users//Administrator//Downloads"],


This should start the Flask Server in your terminal window. By default, it is run on port 80. You can access it by going to,
- **localhost** (on your server's browser)
- **(IP Address of your Server)** (from any other browser on the same network)

For additional features,

- **Password Protection**: Set a password in the config.json file.
- **Hiding Folders**: Add paths of folders to hide in the config.json file as a list.
- **Favorite Folders**: Add paths to add as favorites in the config.json file as a list.
- **Share only Specific Folder**: Give a path to the Root Directory or leave it as default '/' to share the complete computer directory.

## Issues ##

- [x] Change File icons 
- [x] Implement Video Streaming Works Already
- [ ] Implement Back/Forward Button 
- [x] Upload Button	
- [x] Add Upload to specific folders
- [x] Add Download Folder option (Zip folder)
- [x] Add Security Features Added Hiding ()
- [x] change to setup.py 
- [x] Remove inline css to separate css file Partially 
- [x] Add Favorites 
- [x] Fix Mobile CSS 
- [ ] File drop to upload
- [ ] Share only specific folder 
- [ ] Take path from command line
- [x] Add How to find IP Address (ISSUE)
- [ ] Test on Linux
- [ ] Test on Windows
- [x] Test on Mac
- [x] Add Error Handling 
- [x] Add Login Page Current Directory and Password 
- [ ] Add Hidden Validation
- [ ] Add Favorites Validation
- [ ] Add Upload Validation
- [ ] ISSUE: Favorites doesnt work with Limited Directory Usage
- [x] Add Breadcrumb path
- [x] Add a proper Config file for all configrations hidden, favorites, login 
- [x] Add Exit Button
- [x] Describe how to get your own IP address for Mac, Windows, Linux
- [ ] Add username and create a log file to track accesses and each executed instruction
- [x] Add option for selecting available Drives
- [x] Add requirements.txt
- [ ] Better Security
- [x] QR Code File Download
- [x] Performance Improvement by converting Python directory+file code to Jinja

<br>

**Support Me**
-
Like my work? Click on the button below and help me keep caffeinated! ☕️ 🙏🏻

<a href = "https://www.buymeacoffee.com/rehanahmed">
<img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 35px !important;width: 140px !important;"></a>
