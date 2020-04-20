import os
from tkinter import *
from google_drive import *

def file_uploader(full_path, extracted_folder_name, date):
        count = 0
        for filename in os.listdir(full_path):
            if filename.endswith(".mp4"):
                #Create folder if not exist
                if count == 0:
                    folder_id = check_folder_exists(extracted_folder_name)
                #Upload your mp4 file into the folder
                upload_file_inside_folder(extracted_folder_name + " " + date + " part " + str(count)
                , filename, folder_id, full_path)
                count += 1
            else:
                print("file which didn't work", filename)
    
def create_full_path(full_named_folder):
    return path.get() + "\\" + full_named_folder


def read_folder():
    list_folders = os.listdir(path.get())
    for full_named_folder in list_folders:
        date, _, extracted_folder_name = full_named_folder.split(" ",2)
        _, extracted_folder_name = extracted_folder_name[::-1].split(" ", 1)
        extracted_folder_name = extracted_folder_name[::-1]
        
        #go inside the folder so that we can read the files which are ending with .mp4
        full_path = create_full_path(full_named_folder)
        #uploading mp4 files into the respective folders in google drive
        file_uploader(full_path, extracted_folder_name, date)
                
    pathEntry.delete(0, END)
    
    
def main():
    global path, pathEntry
    global main_screen
    main_screen = Tk()
    main_screen.geometry("350x300")
    main_screen.title("File Transfer Application")
    Label(text="").pack()
    Label(text="File Transfer Application", bg="grey", width="350", height="2", font=('Calibri',13)).pack()
    path = StringVar()
    Label(text="").pack()
    Label(main_screen, text="Give Folder Path: *", font=("Calibri", 13)).pack()
    pathEntry = Entry(main_screen, textvariable=path)
    pathEntry.pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Transfer Now", font=("Calibri", 13), height="2", width="15"
          ,command=read_folder).pack()
    
    main_screen.mainloop()

main()