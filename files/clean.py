import os
import shutil
from datetime import date

contentFolder = "/var/www/html"  # Folder to clean
maxSizeGB = 5  # Max folder size
nDaysBeforeExpiration = 30

# Get dir size
dirSizeBytes = 0
for dirPath, dirNames, fileName in os.walk(contentFolder):
    for f in fileName:
        fp = os.path.join(dirPath, f)
        dirSizeBytes += os.path.getsize(fp)

# Clean dir if it is too big
maxSizeBytes = maxSizeGB * 1024 * 1024 * 1024;
if dirSizeBytes > maxSizeBytes:
    # Iterate through years
    nYearsBeforeExpiration = nDaysBeforeExpiration / 30 / 12
    for d in os.listdir(contentFolder):
        fullDirPath = contentFolder + d
        if os.path.isdir(fullDirPath):
            if date.today().year - nYearsBeforeExpiration > int(d):
                print("Deleting " + fullDirPath)
                shutil.rmtree(fullDirPath)

    # Iterate through months
    nMonthsBeforeExpiration = nDaysBeforeExpiration / 30
    yearFolder = contentFolder + str(date.today().year).zfill(4)
    for d in os.listdir(yearFolder):
        fullDirPath = os.path.join(yearFolder, d)
        if os.path.isdir(fullDirPath):
            if date.today().month - nMonthsBeforeExpiration > int(d):
                print("Deleting " + fullDirPath)
                shutil.rmtree(fullDirPath)

    # Iterate through days
    monthFolder = os.path.join(yearFolder, str(date.today().month).zfill(2))
    for d in os.listdir(monthFolder):
        fullDirPath = os.path.join(monthFolder, d)
        if os.path.isdir(fullDirPath):
            if date.today().day - nDaysBeforeExpiration > int(d):
                print("Deleting " + fullDirPath)
                shutil.rmtree(fullDirPath)
else:
    print("Nothing to clean, there is enough space.")
