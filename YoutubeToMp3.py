from pytube import YouTube
import os

os.system("")

class TerminalColors:
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    RESET = '\033[0m'

print(TerminalColors.BRIGHT_GREEN + '\nThis is a tool for converting YouTube videos to MP3\n')

def magic():
    yt = YouTube(str(input("\nEnter the URL of the video you want to download: \n>> " + TerminalColors.BRIGHT_CYAN)))
    
    video = yt.streams.filter(only_audio=True).first()          
    
    destination = "C:/YoutubeToMP3"  
    out_file = video.download(output_path=destination)
    
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    print(TerminalColors.RESET + "\n" + yt.title + TerminalColors.BRIGHT_GREEN + " has been successfully downloaded.\n")
    print(TerminalColors.BRIGHT_CYAN + '------To find the video go to YoutubeToMP3 folder on the C drive------\n')

while (True):
    print(TerminalColors.BRIGHT_YELLOW + '1)' + TerminalColors.BRIGHT_MAGENTA + ' Convert YouTube to MP3\n'+ TerminalColors.BRIGHT_YELLOW + '0)' + TerminalColors.BRIGHT_MAGENTA + ' EXIT')
    try:
        user_input = int(input(TerminalColors.BRIGHT_CYAN + 'Enter option' + TerminalColors.BRIGHT_YELLOW + ' 1 or 0: ' + TerminalColors.RESET))
        match(user_input):
            case 1:
                magic()
            case 0:
                break
            case _:
                print(TerminalColors.BRIGHT_RED + '\n-------', user_input ,'is not a valid option -------\n' + TerminalColors.RESET)  
    except Exception:
        print(TerminalColors.BRIGHT_RED + '\n-------not a valid option-------\n'+ TerminalColors.RESET) 

print(TerminalColors.RESET)
