import os
import platform
import shutil

f = 0

if platform.system() == "Linux" or platform.system() == "Darwin":
    clear = "clear"
else:
    clear = "cls"

os.system(clear)

print("----MODE----")
print("|          |")
print("| [1] COPY |")
print("|          |")
print("| [2] MOVE |")
print("|          |")
print("| [3] VIEW |")
print("|          |")
print("----MODE----")

mode = input("Enter the number for the mode: ")

toCheck = input("Enter the starting directory (C:\Images): ")
copyTo = input("Enter the directory to copy images to: ")

for root, dirs, files in os.walk(toCheck):

    for file in files:

        if file.endswith('.png') or file.endswith('.jpg'):

            if int(mode) == 1:
                if os.path.exists(copyTo + "/Backup") == False:
                    os.system("mkdir " + copyTo + "\BACKUP")
                    
                elif os.path.exists(os.path.join(copyTo, "/Backup", file)) == True:
                    if file.endswith(".jpg"):
                        name = file.replace(".jpg", "")
                        ext = ".jpg"
                    elif file.endswith(".png"):
                        name = file.replace(".png", "")
                        ext = ".png"
                    os.rename(os.path.join(copyTo, "/Backup", file), os.path.join(copyTo, "/Backup", name + str(f)) + ext)
                try:    
                    shutil.copy(os.path.join(root, file), copyTo + "/BACKUP")
                except:
                    print("Permission Denied: " + os.path.join(root, file))

                f += 1

            elif int(mode) == 2:
                if os.path.exists(copyTo + "/Backup") == False:
                    os.system("mkdir " + copyTo + "\BACKUP")
                    
                elif os.path.exists(os.path.join(copyTo, "/Backup", file)) == True:
                    if file.endswith(".jpg"):
                        name = file.replace(".jpg", "")
                        ext = ".jpg"
                    elif file.endswith(".png"):
                        name = file.replace(".png", "")
                        ext = ".png"
                    try:
                        os.rename(os.path.join(copyTo, "/Backup", file), os.path.join(copyTo, "/Backup", name + str(f)) + ext)
                    except:
                        print("Permission Denied: " + os.path.join(root, file))
                try:    
                    shutil.move(os.path.join(root, file), (copyTo + "/BACKUP"))
                except:
                    print("Permission Denied: " + os.path.join(root, file))

                f += 1

            else:
                print(os.path.join(root, file))
                os.system(clear)
                

print(str(f) + " images")
input("Press Enter to exit")
