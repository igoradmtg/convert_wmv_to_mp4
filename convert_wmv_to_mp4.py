import os
dirName = r"z:\001\wmv"
dirNameOut = r"z:\001\Out"
def main():
    files = []
    for r, d, f in os.walk(dirName):
        for file in f:
            if ('.mp4' in file) or ('.mpg' in file) or ('.avi' in file) or ('.wmv' in file) or ('.mkv' in file):
                files.append({'oldName':os.path.join(r,file),'newName':os.path.join(dirNameOut,file.replace('.wmv','.mp4'))})
    print(files)
    for fileName in files:
        print(fileName)
        strExec = f'ffmpeg -i "'+fileName['oldName']+'" -c:v libx264 -crf 18 -profile:v high -r 30 -c:a aac -q:a 100 -ar 48000 "'+fileName['newName']+'"'
        print(strExec)
        os.system(strExec)

if __name__ == '__main__':
    main()
