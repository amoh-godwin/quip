from time import time
import os
from typing import List

from fastapi import APIRouter, File, UploadFile, Form

from dependencies import gif_drive, gif_db


router = APIRouter(prefix='/api/gif_access')

mime_map = {
    '.png': 'image/png',
    '.bmp': 'image/bmp',
    '.gif': 'image/gif',
    '.jpeg': 'image/jpeg',
    '.jpg': 'image/jpeg',
    '.svg': 'image/svg+xml',
    '.tiff': 'image/tiff',
    '.wmf': 'image/wmf'
}


GIFS_DB_MODEL = {
    'name': '',
    'category': ['happy', 'disappointed', 'funny', 'applause', 'sad', 'misc']
}


@router.post('/v1/uploader')
def front_upload(
    happy_files: List[UploadFile] = File(None),
    disappointed_files: List[UploadFile] = File(None),
    funny_files: List[UploadFile] = File(None),
    applause_files: List[UploadFile] = File(None),
    sad_files: List[UploadFile] = File(None),
    misc_files: List[UploadFile] = File(None)
    ):

    for f_obj in happy_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)
        gif_db.put({
           'name': name,
           'category': 'happy'
        })

    for f_obj in disappointed_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)
        gif_db.put({
           'name': name,
           'category': 'disappointed'
        })

    for f_obj in funny_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)
        gif_db.put({
           'name': name,
           'category': 'funny'
        })

    for f_obj in applause_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)
        gif_db.put({
           'name': name,
           'category': 'applause'
        })

    for f_obj in sad_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)
        gif_db.put({
           'name': name,
           'category': 'sad'
        })

    for f_obj in misc_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)
        gif_db.put({
           'name': name,
           'category': 'misc'
        })


    return {'hello': [file.filename for file in happy_files]}
