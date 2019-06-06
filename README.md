# File Explorer Server #

A file explorer that works over local area network (Wi-Fi/Ethernet) using Flask server. You can explore a computer's complete directory and download any file. Moreover, it also lets you stream videos or audio files if your browser supports it.

Server works on,
- Windows
- Linux
- Mac

I have written it in Python using the following web frameworks,

**Frameworks**
-
- Flask (Server)
- Bootstrap 4 

Flask has been used to run the server and serve up the html pages. Meanwhile, Bootstrap has been used to show the Folders and the Files. To open any folder, just click on it and to download/stream any file, just click on it.

![Demo](demo.png)

**How to Run**
-
Clone this repository by using,
    
    git clone https://github.com/reallyrehan/flask-fileexplorer.git

Make sure you have flask installed. You can use the following command to install flask,

    pip install Flask
    
Now, open terminal/command prompt in the flask-fileexplorer directory and run the setup.y file by using the following command,

    python setup.py
    
This should start the Flask Server in your terminal window. You can access it by going to,
- **localhost:5000** (on your server's browser)
- **(IP Address of your Server):5000** (from any other browser on the same network)

Here is how you can find out your PC's IP Address,

- Mac 
- Windows
- Linux
  
