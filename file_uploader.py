def upload(htmldoc, drive, parent_folder_id, title):
    gdoc = drive.CreateFile(
        {
            "parents": [{"kind": "drive#fileLink", "id": parent_folder_id}],
            "title": title,
            "mimeType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        }
    )
    gdoc.SetContentString(htmldoc)
    gdoc.Upload({"convert": True})
    gdoc.InsertPermission({"type": "anyone", "role": "writer", "value": "anyone"})
