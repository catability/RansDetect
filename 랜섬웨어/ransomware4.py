import tkinter
import tkinter.messagebox
import customtkinter

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

import threading, time
import datetime

class App(customtkinter.CTk):
    #myWatcher = Watcher("C:/Temp")


    def __init__(self):
        super().__init__()

        # configure window
        self.title("픽시프록_Ransomware Detector")
        self.geometry(f"{700}x{900}")

        self.center_frame = customtkinter.CTkFrame(self, corner_radius=0)
        #self.center_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self, text="Ransomware Detector", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.logo_label.grid(row=0, column=1, padx=(20, 20), pady=(10, 10))
        #self.logo_label.place(anchor=tkinter.CENTER)

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, width=450)
        self.progressbar_1.grid(row=1, column=1, padx=(90, 0), pady=(10, 10), sticky="nsew")

        self.detect_label = customtkinter.CTkLabel(self, text="랜섬웨어 탐지를 위하여 스타트 버튼을 클릭하세요.", font=customtkinter.CTkFont(size=14)) #, weight="bold"))
        self.detect_label.grid(row=2, column=1, padx=(20, 20), pady=(0, 0))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=660, height=560)
        self.textbox.grid(row=3, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.start_button = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=1, text_color=("gray10", "#DCE4EE"), 
                                                    text="Ransomware Detection Start", font=customtkinter.CTkFont(size=18, weight="bold"), command=self.start_button_event ) #, command=button_event)
        self.start_button.grid(row=4, column=1, padx=(20, 0), pady=(10, 10), sticky="nsew")

        self.end_button = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=1, text_color=("gray10", "#DCE4EE"), 
                                                    text="End Program", font=customtkinter.CTkFont(size=18, weight="bold"), command=self.end_button_event ) #, command=button_event)
        self.end_button.grid(row=5, column=1, padx=(20, 0), pady=(10, 10), sticky="nsew")

        self.progressbar_1.configure(mode="indeterminnate", indeterminate_speed=0.4, progress_color="Brown", corner_radius=40, width=450, height=80)

        self.textbox.insert("0.0", "□ 운영체제 : Windows 10 \n□ 현재일 : 2023.07.11.\n::::: 랜섬웨어 감염 여부를 점검하고 있으며, 탐지 시 아래에 탐지 결과를 나타냅니다. ::::: \n")

    # 랜섬웨어 탐지 시작 버튼 (스레드를 활용하여 탐지 진행)
    def start_button_event(self):
        self.progressbar_1.start()
        self.detect_label.configure(text="랜섬웨어 감염 탐지 중")
        #self.start_thread()
        t1 = threading.Thread(target=self.start_thread())
        #t1.setDaemon(True)
        t1.start()

    # 종료 버튼
    def end_button_event(observer):
        app.quit()
        #observer.stop()
        #observer.join()

    # 스레드로 들어오는 함수
    def start_thread(self):
        # Set the format for logging info
        # Example : 2023-01-24 16:59:45 - Created file: .\New Text Document.txt
        logging.basicConfig(level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')

        # Set format for displaying path
        #path = sys.argv[1] if len(sys.argv) > 1 else '.'
        path = "C:/Temp/"

        # Initialize logging event handler
        event_handler = Handler()

        # Initialize Observer
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)

        # Start the observer
        observer.start()
        print("observer.start()")
    

    # 랜섬웨어 탐지 결과를 나타내는 부분
    def textbox_update_event(self, event_text):
        word_line = event_text.split(",")

        box_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        box_str += ",  Action : " + word_line[0]
        box_str += ",  From : " + word_line[1]
        box_str += ",  To : " + word_line[2]
        box_str += "\n"
        print(box_str)


        # 최초 탐지 시간 및 몇번 탐지 했는지 나타내는 부분
        # C:\ini 폴더 생성 및 폴더 안에 "dection_time.ini"과 "/cnt.ini" 파일 생성
        intvar = 0
        f1 = open('C:/ini/dection_time.ini', 'r')
        t1 = f1.readline()

        if t1 == 0:
            f2 = open('C:/ini/dection_time.ini', 'w')
            f2.write(str(int(time.time())))
            f2.close()   
        else:
            intvar = int(time.time()) - int(t1)        

        if intvar < 1000: # & intvar != 0:
            f3 = open('C:/ini/cnt.ini', 'r')            
            t3 = f3.readline()
            if t3 == "":
                t3 = 0
            else:
                t3 = int(t3) + 1
            f3.close()
            f4 = open('C:/ini/cnt.ini', 'w')     
            f4.write(str(t3))
            f4.close()         
        else:
            f5 = open('C:/ini/cnt.ini', 'w')
            f5.write(str(0))
            f5.close()

            if intvar != 0:
                f5 = open('C:/ini/dection_time.ini', 'w')
                f5.write(str(int(time.time())))
                f5.close()   
        
        f1.close()

        # 탐지 내용 텍스트 박스에 표현
        self.textbox.insert("end", box_str)
        

# class implementing the FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print("on_created")
        # Log method needs Log Level, and second parameter is our message which need to be displayed
        logging.log(logging.INFO, f'{event.event_type} {event.src_path}')
        app.textbox_update_event(f'{event.event_type},{event.src_path}')

    def on_modified(self, event):
        print("on_modified")
        logging.log(logging.INFO, f'{event.event_type} {event.src_path}')
        #app = App()
        
        try:
            app.textbox_update_event(f'{event.event_type},{event.src_path},{event.dest_path}')
        except AttributeError:
            print("event.dest_path")
        
        #app.textbox_update_event(f'{event.event_type},{event.src_path},{event.dest_path}')

    def on_deleted(self, event):
        print("on_deleted")
        logging.log(logging.INFO, f'{event.event_type} {event.src_path}')
        app.textbox_update_event(f'{event.event_type},{event.src_path}')
 
    def on_moved(self, event):
        logging.log(logging.INFO, f'{event.event_type} {event.src_path}')
        print("on_move")        
        app.textbox_update_event(f'{event.event_type},{event.src_path},{event.dest_path}')


if __name__ == "__main__":
    app = App()
    app.mainloop()