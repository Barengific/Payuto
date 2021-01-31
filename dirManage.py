# -*- coding: utf-8 -*-
"""

@author: barengific
"""

import os
from pathlib import Path


subDir = {
    "DOCUMENTS": ['.doc','.docx','.pdf','.rtf','.txt'],
    "AUDIO":['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}
def pickDirectory(val):
    for cate, suffixes in subDir.items():
        for suffix in suffixes:
            if suffix == val:
                return cate
    return 'MISC' #If filetype non-existent in dictionary

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()