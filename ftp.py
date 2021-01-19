from ftplib import FTP

ftp = FTP('ftp.us.debian.org', 'user', 'pass')
ftp.login()

# change into "debian" directory
# ftp.cwd('debian')

# put command for upload
# ftp.voidcmd(cmd)
# ftp.sendcmd(cmd)

ftp.quit()