# What is this?
If you need to deploy changes, but don't want to upload every file with ftp and don't use git auto pull for any reason. Then if you have ssh access to server, script will deploy list of changed files with `scp`.


# How to use?

- Take list of commit changed files with 
``` bash
git show --name-only [commit]
```

- Put them to `files`

- Upload by `scp` to server
``` bash
python3 scp.py
```


# .env settings
`SSH` - ssh destination
`LOCAL_REPO` - path to project on local machine
`REMOTE_REPO` - path to folder with project on remote machine
`REMOTE_FOLDER` - name of the folder with project in REMOTE_REPO


# License

This project is licensed under the terms of the MIT license.