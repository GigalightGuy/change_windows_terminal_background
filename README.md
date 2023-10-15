# Change Windows Terminal background image randomly 

Simple python script to swap Windows Terminal background image randomly (the script picks the image randomly from all the images inside a folder/directory).  

A .env file with **BACKGROUNDS_PATH**(path to directory with the background images) and **SETTINGS_PATH**(path to Windows Terminal's **settings.json** file) defined is needed.  

## Prerequisites  

- [python](https://www.python.org)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## How to use  

Download/clone this repository or simply copy the **change_terminal_bg.py** file.  
Then create a .env file in the same directory as the python script that defines the environment variables `BACKGROUNDS_PATH` and `SETTINGS_PATH` that represent the full path to the directory with the background images and the full path to the Windows Terminal's settings.json file respectively.

The .env file should look something like this:  
```bash
# .env
BACKGROUNDS_PATH=C:/Users/name/path/to/backgrounds/folder/
SETTINGS_PATH=C:/Users/name/AppData/path/to/windows/terminal/settings.json
```

After creating the .env file and adding those environment variables, if you run the python script, it should update your Windows Terminal background image.

For ease of use, you can also create a .bat file that calls your python script for you, so you don't have to call `python change_terminal_bg.py` or `python3 change_terminal_bg.py` everytime.  
```bash
:: bg.bat
@echo off
python change_terminal_bg.py
```

If you create a file called bg.bat in the same directory as the python script like the one above, you can then add the directory where your batch script (.bat) lives to your PATH environment variable and then you can just call `bg` from anywhere in your command line and see your terminal background image change.  
