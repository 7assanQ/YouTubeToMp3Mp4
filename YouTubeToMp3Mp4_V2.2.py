import os
import arabic_reshaper
from pytube import YouTube
from pytube.cli import on_progress 
from bidi.algorithm import get_display

os.system("")

class TerminalColors:
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    RESET = '\033[0m'

destination = "C:/YoutubeToMp3Mp4"

print(TerminalColors.BRIGHT_GREEN + '\nThis is a tool for converting YouTube videos to MP3 and MP4')

def open_folder():
    if os.path.isdir(destination):    
        os.startfile(destination)
        print('\n' + TerminalColors.BRIGHT_GREEN + destination + TerminalColors.BRIGHT_CYAN + ' Opened')
    else:
        print(TerminalColors.BRIGHT_RED + '\n-------Folder' + TerminalColors.BRIGHT_CYAN + ' YoutubeToMp3Mp4' + TerminalColors.BRIGHT_RED + ' cannot be found. Create the folder ' + TerminalColors.BRIGHT_CYAN + destination + TerminalColors.BRIGHT_RED + ' or use option' + TerminalColors.BRIGHT_YELLOW + ' 1' + TerminalColors.BRIGHT_RED + ' or'+ TerminalColors.BRIGHT_YELLOW + ' 2' + TerminalColors.BRIGHT_RED + ' first-------' + TerminalColors.RESET)

def change_destination():
    global destination

    drives_list = [] 
    option = 1
    print(TerminalColors.BRIGHT_CYAN + '\n-------Choose a different drive-------')
    for driveLetter in [chr(i) + ':' for i in range(65,91)]:
        if os.path.exists(driveLetter):
            print(TerminalColors.BRIGHT_YELLOW + str(option) + ') '+ TerminalColors.BRIGHT_MAGENTA + driveLetter[0]) 
            drives_list.append(driveLetter[0])
            option += 1      

    drive_options = ', '.join(str(i) for i in range(1, option - 1)) + ' or ' + str(option - 1)
    try:
        user_input = int(input(TerminalColors.BRIGHT_CYAN + 'Enter option ' + TerminalColors.BRIGHT_YELLOW + drive_options + ': '+ TerminalColors.RESET))    
        if user_input > len(drives_list) or user_input < 1:
            print(TerminalColors.BRIGHT_RED + '\n-------is not a valid option-------\n'+ TerminalColors.RESET) 
        else:
            new_drive = drives_list[user_input - 1]
            destination = new_drive + ':/YoutubeToMp3Mp4' 
            print(TerminalColors.BRIGHT_CYAN + '\nDestination changed to ' + TerminalColors.BRIGHT_GREEN + destination)  

    except Exception:
        print(TerminalColors.BRIGHT_RED + '\n-------is not a valid option-------\n'+ TerminalColors.RESET)        

def print_title(title_text):
    reshaped_text = arabic_reshaper.reshape(title_text)
    bidi_text = get_display(reshaped_text)
    print(TerminalColors.RESET + "\n\n" + bidi_text + TerminalColors.BRIGHT_GREEN + " has been downloaded successfully.")
    print(TerminalColors.BRIGHT_CYAN + '------To find the video go to', destination ,'or choose option 3------')

def mp3_magic():
    global destination

    try:
        user_url = str(input("Enter YouTube URL of the video you want to convert to Mp3: \n>> " + TerminalColors.BRIGHT_CYAN))
        print(TerminalColors.BRIGHT_YELLOW + '\nConverting and Downloading. WAIT...')

        yt = YouTube(user_url, on_progress_callback = on_progress)
        stream = yt.streams.filter(only_audio=True).first()          
        name = str(yt.title) + '.mp3'
        
        if os.path.exists(os.path.join(destination, name)):
            number = 1
            while os.path.exists(os.path.join(destination, f"{os.path.splitext(name)[0]}({number}).mp3")):
                number += 1
            name = f"{os.path.splitext(name)[0]}({number}).mp3"  
            
        stream.download(output_path=destination, filename=name)
        
        print_title(yt.title)
        
    except Exception:
        print(TerminalColors.BRIGHT_RED + '\n-------Failed to download-------'+ TerminalColors.RESET)  

def mp4_magic():
    global destination

    try:
        user_url = str(input("Enter YouTube URL of the video you want to convert to MP4: \n>> " + TerminalColors.BRIGHT_CYAN))
        print(TerminalColors.BRIGHT_YELLOW + '\nConverting and Downloading. WAIT...')

        yt = YouTube(user_url, on_progress_callback = on_progress)
        stream = yt.streams.get_highest_resolution()
        name = str(yt.title) + '.mp4'

        if os.path.exists(os.path.join(destination, name)):
            number = 1
            while os.path.exists(os.path.join(destination, f"{os.path.splitext(name)[0]}({number}).mp4")):
                number += 1
            name = f"{os.path.splitext(name)[0]}({number}).mp4"

        stream.download(output_path=destination, filename=name)
        
        print_title(yt.title)

    except Exception:
        print(TerminalColors.BRIGHT_RED + '\n-------Failed to download-------'+ TerminalColors.RESET)   

def get_info():

    user_url = str(input("Enter YouTube URL of the video you want to know about: \n>> " + TerminalColors.BRIGHT_CYAN))
    yt = YouTube(user_url)
    print(TerminalColors.RESET + '\nVideo title: ' + TerminalColors.BRIGHT_CYAN + str(yt.title))
    print(TerminalColors.RESET + 'Video duration: ' + TerminalColors.BRIGHT_CYAN + str(yt.length) + ' seconds')
    minutes, seconds = divmod(yt.length, 60)
    print(TerminalColors.RESET + 'Video duration: ' + TerminalColors.BRIGHT_CYAN +  str(minutes) + ' minutes and '+ str(seconds) +' seconds')
    print(TerminalColors.RESET + 'Video author: ' + TerminalColors.BRIGHT_CYAN + str(yt.author))
    print(TerminalColors.RESET + 'Video views: ' + TerminalColors.BRIGHT_CYAN + str(yt.views))
    print(TerminalColors.RESET + 'Video rating: ' + TerminalColors.BRIGHT_CYAN + str(yt.rating))
    print(TerminalColors.RESET + 'Video description: ' + TerminalColors.BRIGHT_CYAN + str(yt.description))
    print(TerminalColors.RESET + 'Video thumbnail URL: ' + TerminalColors.BRIGHT_CYAN + str(yt.thumbnail_url))
    print(TerminalColors.RESET + 'Video keywords: ' + TerminalColors.BRIGHT_CYAN + str(yt.keywords))
    print(TerminalColors.RESET + 'Video publish Date: ' + TerminalColors.BRIGHT_CYAN + str(yt.publish_date))
    print(TerminalColors.RESET + 'Video captions: ' + TerminalColors.BRIGHT_CYAN + str(yt.captions)) 

while (True):
    print(TerminalColors.BRIGHT_CYAN + '\n-------Choose an option-------')
    print(TerminalColors.BRIGHT_YELLOW + '1)' + TerminalColors.BRIGHT_MAGENTA + ' YouTube --> MP3\n'+ TerminalColors.BRIGHT_YELLOW + '2)' + TerminalColors.BRIGHT_MAGENTA + ' YouTube --> MP4\n' + TerminalColors.BRIGHT_YELLOW + '3)' + TerminalColors.BRIGHT_MAGENTA + ' Open YouTubeToMp3Mp4 Folder\n'+ TerminalColors.BRIGHT_YELLOW + '4)' + TerminalColors.BRIGHT_MAGENTA + ' Folder path ' + TerminalColors.BRIGHT_GREEN + destination + TerminalColors.BRIGHT_YELLOW + '\n5)' + TerminalColors.BRIGHT_MAGENTA + ' YouTube video information' + TerminalColors.BRIGHT_YELLOW + '\n0)' + TerminalColors.BRIGHT_MAGENTA + ' EXIT')
    try:
        user_input = int(input(TerminalColors.BRIGHT_CYAN + 'Enter option' + TerminalColors.BRIGHT_YELLOW + ' 1, 2, 3, 4, 5 or 0: ' + TerminalColors.RESET))
        match(user_input):
            case 1:
                print(TerminalColors.BRIGHT_CYAN +'\n-------MP3-------' + TerminalColors.RESET)
                mp3_magic()
            case 2:
                print(TerminalColors.BRIGHT_CYAN +'\n-------MP4-------' + TerminalColors.RESET)
                mp4_magic() 
            case 3:
                open_folder()  
            case 4:
                change_destination()  
            case 5:
                print(TerminalColors.BRIGHT_CYAN +'\n-------Video information-------' + TerminalColors.RESET)
                get_info()           
            case 0:
                print(TerminalColors.BRIGHT_CYAN + '\nThank you for using YoutubeToMp3Mp4')
                break
            case _:
                print(TerminalColors.BRIGHT_RED + '\n-------', user_input ,'is not a valid option -------\n' + TerminalColors.RESET)  
    except Exception:
        print(TerminalColors.BRIGHT_RED + '\n-------not a valid option-------\n'+ TerminalColors.RESET) 

print(TerminalColors.RESET)