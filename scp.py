import os
import sys
import subprocess
from decouple import config

# config
SSH = config('SSH', default=False)
LOCAL_REPO = config('LOCAL_REPO', default=False)
REMOTE_REPO = config('REMOTE_REPO', default=False)
if not SSH or not LOCAL_REPO or not REMOTE_REPO:
    sys.exit('Set env vars first.')

# inspect ssh connection
not_connected = subprocess.run(['ssh', SSH, 'whoami'], stdout=subprocess.DEVNULL)
if not_connected.returncode:
    sys.exit("Unable to establish ssh connection.")


files = open("files", "r")
for file in files:
    file = file.strip()

    if not file:
        continue

    os.system(f"scp {LOCAL_REPO}{file} {SSH}:{REMOTE_REPO}{file}")

files.close


# os.system(f"scp -r /home/karulka/Documents/co/python/ftp-uploader/folder {SSH}:{REMOTE_REPO}")
# clear folder
# copy files to folder with recreating directory structure
# scp folder