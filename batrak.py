import rumps
import time
import subprocess
import random
import os
from AppKit import NSSound
from pydub import AudioSegment
import threading
import schedule

tOld = time.ctime()

# SoundFile = "BatrakCalendar/Sounds/Anger"

# for Files in os.listdir(SoundFile):
#     if Files.endswith(".m4a"):
#         m4aFilesPath = os.path.join(SoundFile, Files)
#         wavFilesPath = os.path.join(SoundFile, Files.replace(".m4a", ".wav"))
        
#         audio = AudioSegment.from_file(m4aFilesPath, format="m4a")
        
#         audio.export(wavFilesPath, format="wav")
#         print("ok")
    
    

def BatrakDays(tOld):
    tOld = time.ctime()
    DaysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for Day in range(0, 7):
        
        if tOld.startswith(DaysOfWeek[Day]):
            if Day == 0:
                tNewDay = "Дохуядельник, "
            elif Day == 1:
                tNewDay = "Ебаторник, "
            elif Day == 2:
                tNewDay = "Охуеда, "
            elif Day == 3:
                tNewDay = "Заебтверг, "
            elif Day == 4:
                tNewDay = "Распиздятница, "
            elif Day == 5:
                tNewDay = "Проебота, "
            else :
                tNewDay = "Распизденье, "

    return tNewDay

def BatrakMonth(tOld):
    tOldList = tOld.split()
    MonthOfYear = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for Month in range (0,12):
        if tOldList[1] == MonthOfYear[Month]:
            if Month == 0:
                tNewMonth = " янв. "
            elif Month == 1:
                tNewMonth = " февр. "
            elif Month == 2:
                tNewMonth = " март. "
            elif Month == 3:
                tNewMonth = " апр. "
            elif Month == 4:
                tNewMonth = " май. "
            elif Month == 5:
                tNewMonth = " июнь. "
            elif Month == 6:
                tNewMonth = " июль. "
            elif Month == 7:
                tNewMonth = " авг. "
            elif Month == 8:
                tNewMonth = " сент. "
            elif Month == 9:
                tNewMonth = " окт. "
            elif Month == 10:
                tNewMonth = " нояб. "
            else:
                tNewMonth = " дек. "
                
    return tNewMonth

def BatrakDaysNumbers(tOld):
    tOldList = tOld.split()
    tNewDayNumber = tOldList[2]
    return tNewDayNumber

def BatrakTime(tOld):
    tOldList = tOld.split()
    tOldListStr = [str(num) for num in tOldList]
    tNewTime = [word[:5] for word in tOldListStr]
    tNewTimeNumber = tNewTime[3]
    
    return tNewTimeNumber

def BatrakSound(tOld):
    tOld = time.ctime()
    DaysOfWeekSound = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for DaySound in range(0, 7):
        
        if tOld.startswith(DaysOfWeekSound[DaySound]):
            if DaySound == 0:
                directory = 'BatrakCalendar/Sounds/Mon'
                files = [file for file in os.listdir(directory) if file.endswith(".wav")]
                random_file = random.choice(files)
                tSound = os.path.join(directory, random_file)
            elif DaySound == 1:
                directory = 'BatrakCalendar/Sounds/Tue'
                files = [file for file in os.listdir(directory) if file.endswith(".wav")]
                random_file = random.choice(files)
                tSound = os.path.join(directory, random_file)
            elif DaySound == 2:
                directory = 'BatrakCalendar/Sounds/Wed'
                files = [file for file in os.listdir(directory) if file.endswith(".wav")]
                random_file = random.choice(files)
                tSound = os.path.join(directory, random_file)
            elif DaySound == 3:
                directory = 'BatrakCalendar/Sounds/Thu'
                files = [file for file in os.listdir(directory) if file.endswith(".wav")]
                random_file = random.choice(files)
                tSound = os.path.join(directory, random_file)
            elif DaySound == 4:
                directory = 'BatrakCalendar/Sounds/Fri'
                files = [file for file in os.listdir(directory) if file.endswith(".wav")]
                random_file = random.choice(files)
                tSound = os.path.join(directory, random_file)
            elif DaySound == 5:
                directory = 'BatrakCalendar/Sounds/Sat'
                files = [file for file in os.listdir(directory) if file.endswith(".wav")]
                random_file = random.choice(files)
                tSound = os.path.join(directory, random_file)
            else :
                directory = 'BatrakCalendar/Sounds/Sun'
                files = [file for file in os.listdir(directory) if file.endswith(".wav")]
                random_file = random.choice(files)
                tSound = os.path.join(directory, random_file)

    return tSound

def BatrakSoundButton(tOld):
    tOld = time.ctime()
    DaysOfWeekSoundButton = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for DaySoundButton in range(0, 7):
        
        if tOld.startswith(DaysOfWeekSoundButton[DaySoundButton]):
            if DaySoundButton == 0:
                tSoundButton = "Опять работа?"
            elif DaySoundButton == 1:
                tSoundButton = "Что мне делать...?"
            elif DaySoundButton == 2:
                tSoundButton= "Моя жизнь пренадлежить орде."
            elif DaySoundButton == 3:
                tSoundButton = "Ыгыы"
            elif DaySoundButton == 4:
                tSoundButton = "Пивка для рывка!"
            elif DaySoundButton == 5:
                tSoundButton = "Золотой рудник обрушился!"
            else :
                tSoundButton = "Пора... просыпаться"

    return tSoundButton

def BatrakWaitingSound():
    WaitingDirectory = "BatrakCalendar/Sounds/Waiting"
    files = [file for file in os.listdir(WaitingDirectory) if file.endswith(".wav")]
    random_file = random.choice(files)
    tSoundWaiting = os.path.join(WaitingDirectory, random_file)
    return tSoundWaiting

def BatrakAngerSound():
    WaitingDirectory = "BatrakCalendar/Sounds/Anger"
    files = [file for file in os.listdir(WaitingDirectory) if file.endswith(".wav")]
    random_file = random.choice(files)
    tSoundWaiting = os.path.join(WaitingDirectory, random_file)
    return tSoundWaiting
    

class BatrakApp(rumps.App):
    def __init__(self):
        tOld = time.ctime()
        super(BatrakApp, self).__init__("CC")
        self.menu = [rumps.MenuItem("Скоро будет анекдот")]
        self.title = self.update_title()
        self.timer_title = rumps.Timer(self.update_title, 1)
        self.timer_menu = rumps.Timer(self.update_menu, 86400)
        threading.Timer(600, self.play_sound).start()
        schedule.every(1).hour.do(self.play_sound_waiting)
        self.timer_title.start()
        self.timer_menu.start()
        subprocess.Popen(['afplay', BatrakSound(tOld)])

    @rumps.clicked(BatrakSoundButton(tOld))
    def play_sound(self, _=None):
        sound = NSSound.alloc()
        sound.initWithContentsOfFile_byReference_(BatrakSound(tOld), True)
        sound.play()
        
    @rumps.clicked("НЕ НАЖИМАЙ!")
    def on_menu_item_clicked(self, _):
        sound = NSSound.alloc()
        sound.initWithContentsOfFile_byReference_(BatrakAngerSound(), True)
        sound.play()
    
    def play_sound_waiting(self):
        sound = NSSound.alloc()
        sound.initWithContentsOfFile_byReference_(BatrakWaitingSound(), True)
        sound.play()
        
    def update_menu(self, _=None):
        tOld = time.ctime()
  
    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)
    threading.Thread(target=run_schedule).start()
 
    def update_title(self, _=None):
        tOld = time.ctime()
        new_title = BatrakDays(tOld) + BatrakDaysNumbers(tOld) + BatrakMonth(tOld) + BatrakTime(tOld)
        self.title = new_title

    def menu_update(self, _):
        self.update_title(None)
        self.update_menu(None)


if __name__ == '__main__':
    app = BatrakApp()
    app.run()