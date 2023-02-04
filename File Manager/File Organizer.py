#%%
import os
import shutil

try:
    # USE STRIP() TO REMOVE THE QUOTES FROM THE FILE NAME
    # "C:\Users\mehar_uslilw0\Downloads\SampleAudio.mp3"
    #  "C:\Users\mehar_uslilw0\Downloads\SampleTextFile.txt"
    file_name = input("Enter file name: ").strip('""')
    # SPLIT THE FILE NAME BY THE DOT AND SELECT THE SECOND ITEM FROM THE LIST, WHICH IS THE EXTENSION
    extension = file_name.split(".")[1]
    print(extension)
except FileNotFoundError:
    print("OOPS! FILE DOES NOT EXIST!")

dstFile1 = "C:/Users/mehar_uslilw0/VS Codes/Text File"
dstFile2 = "C:/Users/mehar_uslilw0/VS Codes/Audio_Video File"
dstFile3 = "C:/Users/mehar_uslilw0/VS Codes/Document File"
dstFile4 = "C:/Users/mehar_uslilw0/VS Codes/exe_zip_rar File"
dstFile5 = "C:/Users/mehar_uslilw0/VS Codes/Image File"
dstFile6 = "C:/Users/mehar_uslilw0/VS Codes/HTML File"
dstFile7 = "C:/Users/mehar_uslilw0/VS Codes/Other Formats File"

if extension == "csv" or extension == "txt":
    if not os.path.exists(dstFile1):
        os.makedirs(dstFile1)
    shutil.move(src = file_name, dst= dstFile1)

elif extension == "mp3" or extension == "mp4":
    if not os.path.exists(dstFile2):
        os.makedirs(dstFile2)
    shutil.move(file_name, dstFile2)    

elif extension == "docx" or extension == "pdf" or extension == "pptx":
    if not os.path.exists(dstFile3):
        os.makedirs(dstFile3)
    shutil.move(src = file_name, dst= dstFile3)

elif extension == "exe" or extension == "zip" or extension == "rar":
    if not os.path.exists(dstFile4):
        os.makedirs(dstFile4)
    shutil.move(src = file_name, dst= dstFile4)

elif extension == "gif" or extension == "jpg" or extension == "jpeg" or extension == "png":
    if not os.path.exists(dstFile5):
        os.makedirs(dstFile5)
    shutil.move(src = file_name, dst= dstFile5)

elif extension == "htm" or extension == "html":
    if not os.path.exists(dstFile6):
        os.makedirs(dstFile6)
    shutil.move(src = file_name, dst= dstFile6)

else:
    if not os.path.exists(dstFile7):
        os.makedirs(dstFile7)
    shutil.move(src= file_name, dst= dstFile7)    


# there is a built-in function in Python called os.path.splitext 
# used to split a file path into the file name and extension


root, ext = os.path.splitext(file_name)

# csv Comma-separated values file
# docx Microsoft Word document
# exe Executable program file
# gif Graphical Interchange Format file
# htm, html Hypertext markup language page
# jpg, jpeg Joint Photographic Experts Group photo file
# mp3 MPEG layer 3 audio file
# mp4 MPEG 4 video
# pdf Portable Document Format file
# png Portable Network Graphics file
# pptx Microsoft PowerPoint presentation
# rar Roshal Archive compressed file
# txt Unformatted text file
# zip Compressed file

# %%
