import shutil
shutil.copy('/root/spam.txt','/home')
shutil.copytree('/root/spam','/root/spam_backup')

# Move function is similar to the Linux one
shutil.move('/root/a.txt','/root/b.txt')

