from pydrive2.drive import GoogleDrive


def create_folder(drive: GoogleDrive, title: str):
    folder_metadata = {'title': title, 'mimeType': 'application/vnd.google-apps.folder'}
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    folder.InsertPermission({"type": "anyone", "role": "writer", "value": "anyone"})
    print(folder["alternateLink"])
    return folder['id']
