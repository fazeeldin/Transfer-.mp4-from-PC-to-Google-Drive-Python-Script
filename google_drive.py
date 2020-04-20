from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def create_folder(folder_name):
    '''
    This function is used to create a new folder in the Google drive.
    The function returns the newly created folder's id.
    '''
    folder = drive.CreateFile({'title': folder_name, "mimeType": "application/vnd.google-apps.folder"})  # Name of the file in my google drive that I want to have
    folder.Upload()
    return folder['id']

def check_folder_exists(folder_name):
    '''
    This function is used to check if a folder exists in the google drive. If it exists,
    then folder_id of that existing folder is returned.
    If the folder doesn't exist, then create_folder function is called. It will create
    the folder in the google drive and will return the newly created folder's id.
    '''
    list_of_file = drive.ListFile({'q':"'root' in parents and trashed=false"}).GetList()
    for drive_folder in list_of_file:
        if drive_folder['title'] == folder_name:
            return drive_folder['id']
    else:
        folder_id = create_folder(folder_name)
        return folder_id

def upload_file(title, filename, fid, full_path):
    file = drive.CreateFile({'title': title})  # Name of the file in my google drive that I want to have
    file.SetContentFile(full_path + "\\" + filename) # Location and name of the file from where I have to get the file.
    file.Upload()
    return True

def upload_file_inside_folder(title, filename, fid, full_path):
    
    file = drive.CreateFile({'title': title, 
                             "parents": [{"kind": "drive#fileLink", "id": fid}]})  # Name of the file in my google drive that I want to have
    file.SetContentFile(full_path + "\\" + filename) # Location and name of the file from where I have to get the file.
    file.Upload()
    return True