import tkinter as tk
import os
import arabic_reshaper
import pyperclip
from tkinter import ttk
from pytube import YouTube
from bidi.algorithm import get_display

destination = 'C:/YoutubeToMp3Mp4'
available_drives = []
language = True


for driveLetter in [chr(i) + ':' for i in range(65,91)]:
    if os.path.exists(driveLetter):
        available_drives.append(driveLetter[0])

def change_language():
    global language

    if not language:
        lable_1.config(text = 'أدخل رابط اليوتيوب هنا')
        button_1.config(text='MP3 اضغط لتحميل الصوت')
        button_2.config(text='MP4 اضغط لتحميل الفيديو')
        lable_2.config(text='اختر محرك الأقراص')
        button_3.config(text='افتح المجلد\nYouTubeToMp3Mp4')
        button_5.config(text='لصق')
        download_number_1.config(text= '%0 :تحميل')
        feedback = 'أداة لتحويل يوتيوب إلى فيديو أو صوت'
        feedback_message(feedback , 'black')
        language = True
    else:
        lable_1.config(text = 'Enter YouTube URL here')
        button_1.config(text='Click to download Mp3')
        button_2.config(text='Click to download Mp4')
        lable_2.config(text='Choose a drive')
        button_3.config(text='Opne folder\nYouTubeToMp3Mp4')
        button_5.config(text='Paste')
        download_number_1.config(text='Loading: 0%')
        feedback = 'A tool for converting YouTube to mp3 or mp4'
        feedback_message(feedback , 'black')
        language = False
     
def open_folder():
    global destination, language

    destination = user_drive.get() + ':/YoutubeToMp3Mp4'
    try: 
        if os.path.isdir(destination):    
            os.startfile(destination)
            if language:
                feedback = destination + ' افتح'
                feedback_message(feedback, 'green')
            else:    
                feedback = destination + ' opened'
                feedback_message(feedback, 'green')
        else:
            if language:
                feedback = 'YoutubeToMp3Mp4 لا يمكن العثور على المجلد.\n' + destination + ' قم بإنشاء المجلد' +'\n'+ 'أولاً mp3 أو mp4 أو استخدم الخيار'
                feedback_message(feedback, 'red')
            else:
                feedback = 'Folder YoutubeToMp3Mp4 cannot be found.\nCreate the folder ' + destination + '\nor use option mp3 or mp4 first'
                feedback_message(feedback, 'red')    
    except Exception:
        if language:
            feedback = 'لا يمكن فتح المجلد'
            feedback_message(feedback, 'red')
        else:    
            feedback = 'Cannot open the folder'
            feedback_message(feedback, 'red')

def clean_filename(filename):
    illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    
    cleaned_filename = ''
    for char in filename:
        if char not in illegal_chars and ord(char) >= 32:
            cleaned_filename += char
    return cleaned_filename 

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_down = total_size - bytes_remaining
    percentage = str(int(bytes_down / total_size * 100))

    if language:
        download_number_1.config(text= '%' + percentage + ' :تحميل') 
        download_number_1.update()
    else:
        download_number_1.config(text= 'Loading: ' + percentage + '%') 
        download_number_1.update()

    download_bar_1['value'] = int(percentage)

def mp3_magic():
    global destination, language

    destination = user_drive.get() + ':/YoutubeToMp3Mp4'

    try:
        user_url = textbox_1.get('1.0', tk.END)

        yt = YouTube(user_url, on_progress_callback = on_progress)
        stream = yt.streams.filter(only_audio=True).first()          
        name = clean_filename(str(yt.title)) + '.mp3'
        
        if os.path.exists(os.path.join(destination, name)):
            number = 1
            while os.path.exists(os.path.join(destination, f"{os.path.splitext(name)[0]}({number}).mp3")):
                number += 1
            name = f"{os.path.splitext(name)[0]}({number}).mp3"  
            
        stream.download(output_path=destination, filename=name)
        if language:
            feedback = yt.title + '\n بنجاح mp3 تم تحميل'
            feedback_message(feedback, 'green')
        else:
            feedback = yt.title + '\nmp3 has been downloaded successfully'
            feedback_message(feedback, 'green')
        
    except Exception:
        if language:
            feedback = 'فشل في التحميل'
            feedback_message(feedback, 'red')
        else:
            feedback = 'Failed to download'
            feedback_message(feedback, 'red')

def mp4_magic():
    global destination, language

    destination = user_drive.get() + ':/YoutubeToMp3Mp4'

    try:
        user_url = textbox_1.get('1.0', tk.END)

        yt = YouTube(user_url, on_progress_callback = on_progress)
        stream = yt.streams.get_highest_resolution()

        name = clean_filename(str(yt.title)) + '.mp4'
        
        if os.path.exists(os.path.join(destination, name)):
            number = 1
            while os.path.exists(os.path.join(destination, f"{os.path.splitext(name)[0]}({number}).mp4")):
                number += 1
            name = f"{os.path.splitext(name)[0]}({number}).mp4"

        stream.download(output_path=destination, filename=name)
        
        if language:
            feedback = yt.title + '\n بنجاح mp4 تم تحميل'
            feedback_message(feedback, 'green')
        else:
            feedback = yt.title + '\nmp4 has been downloaded successfully'
            feedback_message(feedback, 'green')   
        
    except Exception:
        if language:
            feedback = 'فشل في التحميل'
            feedback_message(feedback, 'red')
        else:
            feedback = 'Failed to download'
            feedback_message(feedback, 'red')   

def feedback_message(feedback, color):
    reshaped_text = arabic_reshaper.reshape(feedback)
    bidi_text = get_display(reshaped_text)

    lable_feedback.config(state='normal')
    lable_feedback.delete('1.0', tk.END)
    lable_feedback.insert('1.0', bidi_text)
    lable_feedback.config(foreground = color)
    lable_feedback.config(state='disabled')

#this is base64 of the tool icon. this is a very low quality png with size 32x32 and 444 bytes = 3552 bits. base64 string contains 6 bits in each character so 3552/6 = 592. which is the following icon string 
icon = 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAB7UExURUdwTP8aGv8DAwICAoaGhv///ywsLP///y8vL////wEBAX19ff///3d3d5OTk1VVVf///1dXV1NTU1lZWZOTk////3Nzc3h4eP////8AAAAAAPYAADoCAvwAAJmZmRoQEPUAALm5uaSkpIKCgpMBAU4GBnZubjUjI0tKSn+VKt0AAAAZdFJOUwDi+/1fCMsByAT+ZANpQFoGVVxWRwltagKx7zC4AAAAuklEQVQ4y61T2RLCIAyMtpa23rdZ79v//0IfkCkNFOooL2TIsrk2RF8fxPz41Q9gFQAkIAV4aZS+SmgiJf0zjOwkcszFf0zqDz3BgVxS5vAV120q+GMzc8fb0mEFYK4AqcPGbEOsGCZjZhtSwIm2Oxwfl9f1/jyLJIy13WuC20kCCl+IAdonmfrL7LdvVLzVhEwOK4MY9zI8bprqgRveBcaO5LQPZU2BjqI3hCSg6TUaFP3HxYpurue8AaETEU9VM/8PAAAAAElFTkSuQmCC'
app = tk.Tk()
app.iconphoto(True, tk.PhotoImage(data=icon))
app.geometry('620x300')
app.resizable(False, False)
app.title('YouTubeToMp3Mp4')
app.config(bg = 'antique white')


lable_feedback = tk.Text(app, height=3, width=45, font=('Arial', 12), background='antique white', borderwidth=0)
lable_feedback.place(x = 200, y = 220)
feedback = 'أداة لتحويل يوتيوب إلى فيديو أو صوت'
feedback_message(feedback , 'black')

lable_1 = tk.Label(app, text='أدخل رابط اليوتيوب هنا', font=('Arial', 18), background='antique white')
lable_1.pack(pady = 10)

textbox_1 = tk.Text(app, height=2, width=60, font=('Arial', 12), foreground='steelBlue4', background='gray90')
textbox_1.place(x = 10, y = 60)

button_1 = tk.Button(app, text='MP3 اضغط لتحميل الصوت', font=('Arial', 12), background='light blue', command= mp3_magic)
button_1.place(x = 250, y = 120)

button_2 = tk.Button(app, text='MP4 اضغط لتحميل الفيديو', font=('Arial', 12), background='light blue', command= mp4_magic)
button_2.place(x = 430, y = 120)

lable_2 = tk.Label(app, text='اختر محرك الأقراص', font=('Arial', 16), foreground='white', background='dark red')
lable_2.place(x = 15, y = 210)

user_drive = tk.StringVar()
user_drive.set(available_drives[0])

drop_menu1 = tk.OptionMenu(app, user_drive , *available_drives)
drop_menu1.place(x = 60, y = 240)
drop_menu1.config(font=('Arial', 14), background='dark red', foreground='white')

button_3 = tk.Button(app, text='افتح المجلد\nYouTubeToMp3Mp4', font=('Arial', 12), background ='light blue', command = open_folder)
button_3.place(x = 10, y = 110)

button_4 = tk.Button(app, text='عربي\nEnglish', font=('Arial', 10, 'bold'), background ='dark red', foreground= 'white', command = change_language)
button_4.place(x = 10, y = 5)

download_bar_1 = ttk.Progressbar(app, orient='horizontal', mode='determinate', length=335)
download_bar_1.place(x = 250, y = 175)

def update_download_number():
    return '%0 :تحميل'

download_number_1 = tk.Label(app, text = update_download_number(), foreground='green', background='antique white')
download_number_1.place(x = 160, y = 175)

def paste():
    textbox_1.delete('1.0', tk.END)
    textbox_1.insert('1.0', pyperclip.paste())

button_5 = tk.Button(app, text='لصق', font=('Arial', 11, 'bold'), background ='light blue', command = paste)
button_5.place(x = 560, y = 63)

app.mainloop()