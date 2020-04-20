# Transfer-.mp4-from-PC-to-Google-Drive-Python-Script
## Inspiration:

I am an online trainer. I record the live session for my student's future rerference on zoom meeting. For every meeting, 
a folder is created with a specific naming convention in my documents/zoom folder

Source File Name Convention: DATE TIME NAME_OF_THE_MEETING MEETING_ID.

I have to upload these files on Google Drive every day after the class is complete. The file needs to be uploaded in the folder. 
The name of the folder should be the NAME_OF_THE_MEETING (Refer above). The name of the file in the drive has a specific naming 
convention too.

Destination File Name Convention: NAME_OF_THE_MEETING DATE PART_i, where i value ranges between 0 to as many .mp4 files as there are in
the input source folder.


## FRONTEND
TKINTER

## BACKEND
Python 3.7

## PACKAGES USED
PyDrive

## Things to take care of
1. Generate Google Drive Api and download client_secrets.json file from your Google Dev Console. The json file should be kept in your
working directory.
2. google_drive.py and main.py should be in the same folder.

# Step
1. Run main.py.
2. This will open up an authentication page in your default browser. Accept and add your project.
3. Now a desktop window will open.
4. Give the input link.
5. Click "Transfor Now" button.
6. Your file will be uploaded. Based on your internet speed, it may take some time.
