from pyprojroot import here
import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


# write_creds()
def auth():
    secret_file = here(os.getenv("GOOGLE_CREDENTIALS_FILENAME"))

    settings = {
        "client_config_backend": "service",
        "service_config": {
            "client_json_file_path": secret_file,
        }
    }

    gauth = GoogleAuth(settings=settings)
    gauth.ServiceAuth()
    drive = GoogleDrive(gauth)
    return drive
