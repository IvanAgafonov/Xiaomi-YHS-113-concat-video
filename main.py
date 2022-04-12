import os

disk = input("disk: ")

folders = os.listdir(disk + ":/record")
folders.sort()
file_names = ""
for folder in folders:
    files = os.listdir(disk + ":/record/" + folder)
    for file in files:
        if ".tmp" not in file and ".mp4" in file:
            file_names += "file " + disk + ":/record/" + folder + "/" + file + "\n"

list_files = open("list.txt", "w")
list_files.write(file_names)
list_files.close()
cmd = "ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4"
os.system(cmd)
