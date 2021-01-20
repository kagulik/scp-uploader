import os
import shutil
import sys
import subprocess
from decouple import config

# config
SSH = config('SSH', default=False)
LOCAL_REPO = config('LOCAL_REPO', default=False)
REMOTE_REPO = config('REMOTE_REPO', default=False)
REMOTE_FOLDER = config('REMOTE_FOLDER', default=False)
if not SSH or not LOCAL_REPO or not REMOTE_REPO or not REMOTE_FOLDER:
    sys.exit('Set env vars first.')

# inspect ssh connection
not_connected = subprocess.run(['ssh', SSH, 'whoami'], stdout=subprocess.DEVNULL)
if not_connected.returncode:
    sys.exit("Unable to establish ssh connection.")

# replace ~ with full path
LOCAL_REPO = os.path.expanduser(LOCAL_REPO)

# copy files to folder with recreating directory structure
files = open("files", "r")
for file in files:
    file = file.strip()

    if not file:
        continue

    os.makedirs(os.path.dirname(f"folder/{file}"), exist_ok=True)
    shutil.copy(f"{LOCAL_REPO}{file}", f"folder/{file}")

files.close

# rename folder to REMOTE_FOLDER
os.rename('folder', REMOTE_FOLDER)

# scp folder
result = os.system(f"scp -r {REMOTE_FOLDER} {SSH}:{REMOTE_REPO}")

# clear folder
shutil.rmtree(REMOTE_FOLDER)

# create empty folder
os.mkdir('folder')