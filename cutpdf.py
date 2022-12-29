import os
from pdf2image import convert_from_path

# folder path
dir_path = r'.\\PDF\\'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    
    if os.path.isfile(os.path.join(dir_path, path)) and path.lower().endswith(('.pdf')):
        images = convert_from_path(os.path.join(dir_path, path), 50 , poppler_path = r"C:\ProgramData\chocolatey\lib\poppler\tools")

        for image in images:
            image.save('.\\output\\'+str(path)[:-4]+'.png')
            #print(image)
            break
        
        res.append(path)
        print("Processed "+path.lower()+" to "+str(path)[:-4]+'.png')
print(res)
