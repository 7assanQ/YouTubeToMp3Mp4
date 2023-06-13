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

print(TerminalColors.BRIGHT_GREEN + '\nThis is a tool for converting YouTube videos to MP3 and MP4\n')

def open_folder():
    if os.path.isdir('C:/YoutubeToMp3Mp4'):    
        os.startfile('C:/YoutubeToMp3Mp4')
        print('')
    else:
        print(TerminalColors.BRIGHT_RED + '\n-------Folder' + TerminalColors.BRIGHT_CYAN + ' YoutubeToMp3Mp4' + TerminalColors.BRIGHT_RED + ' cannot be found. Create the folder on the' + TerminalColors.BRIGHT_CYAN +' C' + TerminalColors.BRIGHT_RED + ' drive or use option' + TerminalColors.BRIGHT_YELLOW + ' 1' + TerminalColors.BRIGHT_RED + ' or'+ TerminalColors.BRIGHT_YELLOW + ' 2' + TerminalColors.BRIGHT_RED + ' first-------\n' + TerminalColors.RESET)

def print_title(title_text):
    reshaped_text = arabic_reshaper.reshape(title_text)
    bidi_text = get_display(reshaped_text)
    print(TerminalColors.RESET + "\n\n" + bidi_text + TerminalColors.BRIGHT_GREEN + " has been downloaded successfully.\n")
    print(TerminalColors.BRIGHT_CYAN + '------To find the video go to YoutubeToMp3Mp4 folder on the C drive or choose option 3------\n')

def file_name(number, base, out_file, extention):
    try:
        base = base + str('(' + str(number) + ')')
        new_file = base + extention
        os.rename(out_file, new_file)
        return False
    except Exception:  
        return True
    

def mp3_magic():
    try:
        user_url = str(input("\nEnter the URL of the video you want to convert to Mp3: \n>> " + TerminalColors.BRIGHT_CYAN))
        print(TerminalColors.BRIGHT_YELLOW + '\nConverting and Downloading. WAIT...')
        yt = YouTube(user_url, on_progress_callback = on_progress)
        
        video = yt.streams.filter(only_audio=True).first()          
        
        destination = "C:/YoutubeToMp3Mp4"  
        out_file = video.download(output_path=destination)
        
        base, ext = os.path.splitext(out_file)

        try:
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        except Exception:     
            stop = True
            number = 1
            while stop:
                stop = file_name(number, base, out_file, '.mp3')  
                number += 1
        
        print_title(yt.title)
        
    except Exception:
        print(TerminalColors.BRIGHT_RED + '\n-------Failed to download-------\n'+ TerminalColors.RESET)  

def mp4_magic():
    try:
        user_url = str(input("\nEnter the URL of the video you want to convert to MP4: \n>> " + TerminalColors.BRIGHT_CYAN))
        print(TerminalColors.BRIGHT_YELLOW + '\nConverting and Downloading. WAIT...')
        yt = YouTube(user_url, on_progress_callback = on_progress)

        video = yt.streams.get_highest_resolution()

        destination = "C:/YoutubeToMp3Mp4"  
        out_file = video.download(output_path=destination)
        
        base, ext = os.path.splitext(out_file)

        try:
            new_file = base + '.mp4'
            os.rename(out_file, new_file)
        except Exception:     
            stop = True
            number = 1
            while stop:
                stop = file_name(number, base, out_file, '.mp4')  
                number += 1
        
        print_title(yt.title)

    except Exception:
        print(TerminalColors.BRIGHT_RED + '\n-------Failed to download-------\n'+ TerminalColors.RESET)           

while (True):
    print(TerminalColors.BRIGHT_YELLOW + '1)' + TerminalColors.BRIGHT_MAGENTA + ' Convert YouTube to MP3\n'+ TerminalColors.BRIGHT_YELLOW + '2)' + TerminalColors.BRIGHT_MAGENTA + ' Convert YouTube to MP4\n' + TerminalColors.BRIGHT_YELLOW + '3)' + TerminalColors.BRIGHT_MAGENTA + ' Open YouTubeToMp3Mp4 Folder\n'+ TerminalColors.BRIGHT_YELLOW + '0)' + TerminalColors.BRIGHT_MAGENTA + ' EXIT')
    try:
        user_input = int(input(TerminalColors.BRIGHT_CYAN + 'Enter option' + TerminalColors.BRIGHT_YELLOW + ' 1, 2, 3, or 0: ' + TerminalColors.RESET))
        match(user_input):
            case 1:
                mp3_magic()
            case 2:
                mp4_magic() 
            case 3:
                open_folder()   
            case 0:
                break
            case _:
                print(TerminalColors.BRIGHT_RED + '\n-------', user_input ,'is not a valid option -------\n' + TerminalColors.RESET)  
    except Exception:
        print(TerminalColors.BRIGHT_RED + '\n-------not a valid option-------\n'+ TerminalColors.RESET) 

print(TerminalColors.RESET)
