import os
print(os.path.abspath('spam.png'))
print(os.path.isabs('spam.png'))
# The result: pic/spam.png
print(os.path.relpath(r'/root/pic/spam.png',r'/root'))
# dirname and basename
# exists, isdir, isfile, getsize, listdir, makedirs

# calculate the whole folder's files' size
for filename in os.listdir(r'/root/automatebook'):
    if not os.path.isfile(os.path.join(r'/root/automatebook',filename)):
        continue 
    totalSize = totalSize + os.path.getsize (os.path.join(r'/root/automatebook', filename))
print(totalSize)

# delete
# current dir
os.getcwd()
os.unlink(filename)
shutil.rmtree('dir') # delete the whole folder

# send2trash package
send2trash.send2trash(filename)

# dangerous, do not forget to dry run

# os.walk
for folderName, subfolders, filenames in os.walk('/root/meme'):
    print('The folder is' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)
    
    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(foldername, file), os.join(foldername, file + '.backup')
