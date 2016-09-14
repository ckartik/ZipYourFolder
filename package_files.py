import os;
import zipfile;
import shutil;
import datetime;

# RM - This is stable and accepted as version 1.0 - 11/08/2016

def zipdir(currentDir, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(currentDir):
        if root.endswith('ZippedVersions'):
            print("ZippedVersions")
        else:     
            for file in files:
                rt = root
                rt = rt.replace(currentDir, './')
                ziph.write(os.path.join(rt, file))
                print("zipping", str(os.path.join(rt, file)), "to", rt)


if __name__ == '__main__':
    fileName = "ADD_NAME_YOU_WANT_FOR_ZIP" + datetime.datetime.now().isoformat() + ".zip"
    path = os.getcwd()
    newPath = os.path.join(os.getcwd(), 'ZippedVersions');
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    zipf = zipfile.ZipFile(os.path.join(newPath, fileName), 'w', zipfile.ZIP_STORED)
    zipdir(path, zipf)
    zipf.printdir()
    zipf.close()
