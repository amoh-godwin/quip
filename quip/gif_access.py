from posixpath import relpath
from time import time
import os
from typing import List

from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import StreamingResponse

from dependencies import gif_drive, gif_db


router = APIRouter(prefix='/api/gif_access')

mime_map = {
    '.png': 'image/png',
    '.bmp': 'image/bmp',
    '.gif': 'image/gif',
    '.jpeg': 'image/jpeg',
    '.jpg': 'image/jpg',
    '.svg': 'image/svg+xml',
    '.tiff': 'image/tiff',
    '.wmf': 'image/wmf',
    '.mp4': "video/mp4"
}


GIFS_DB_MODEL = {
    'name': '',
    'category': ['happy', 'disappointed', 'funny', 'applause', 'sad', 'misc'],
    'thumbnail': ""
}


@router.get('/list')
def list_drive():
    a_o_i = gif_drive.list()
    return {'all': a_o_i}

@router.get('/delete')
def delete_drive():
    a_o_i = gif_drive.list()
    names = a_o_i['names']
    ret = gif_drive.delete_many(names)
    return {'all': ret}

@router.post('/v1/uploader')
def front_upload(
    happy_files: List[UploadFile] = File(None),
    happy_thumbs: List[UploadFile] = File(None),
    disappointed_files: List[UploadFile] = File(None),
    disappointed_thumbs: List[UploadFile] = File(None),
    funny_files: List[UploadFile] = File(None),
    funny_thumbs: List[UploadFile] = File(None),
    applause_files: List[UploadFile] = File(None),
    applause_thumbs: List[UploadFile] = File(None),
    sad_files: List[UploadFile] = File(None),
    sad_thumbs: List[UploadFile] = File(None),
    misc_files: List[UploadFile] = File(None),
    misc_thumbs: List[UploadFile] = File(None)
    ):

    status = 'All is well'

    happy_thumbs_map = {}
    disappointed_thumbs_map = {}
    funny_thumbs_map = {}
    applause_thumbs_map = {}
    sad_thumbs_map = {}
    misc_thumbs_map = {}

    for f_obj in happy_thumbs:
        if not f_obj.filename:
            continue
        key = f_obj.filename
        value = f_obj.file
        happy_thumbs_map[key] = value

    for f_obj in disappointed_thumbs:
        if not f_obj.filename:
            continue
        key = f_obj.filename
        value = f_obj.file
        disappointed_thumbs_map[key] = value

    for f_obj in funny_thumbs:
        if not f_obj.filename:
            continue
        key = f_obj.filename
        value = f_obj.file
        funny_thumbs_map[key] = value

    for f_obj in applause_thumbs:
        if not f_obj.filename:
            continue
        key = f_obj.filename
        value = f_obj.file
        applause_thumbs_map[key] = value

    for f_obj in sad_thumbs:
        if not f_obj.filename:
            continue
        key = f_obj.filename
        value = f_obj.file
        sad_thumbs_map[key] = value

    for f_obj in misc_thumbs:
        if not f_obj.filename:
            continue
        key = f_obj.filename
        value = f_obj.file
        misc_thumbs_map[key] = value

    for f_obj in happy_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)

        if ext == '.mp4':
            thumb_name = f_obj.filename.replace(ext, '.jpg')
            data = happy_thumbs_map[thumb_name]
            thumb_name = name.replace(ext, '.jpg')
            gif_drive.put(thumb_name, data)
        else:
            thumb_name = name

        gif_db.put({
           'name': name,
           'category': 'happy',
           'thumbnail': thumb_name
        })

    for f_obj in disappointed_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)

        if ext == '.mp4':
            thumb_name = f_obj.filename.replace(ext, '.jpg')
            data = disappointed_thumbs_map[thumb_name]
            thumb_name = name.replace(ext, '.jpg')
            gif_drive.put(thumb_name, data)
        else:
            thumb_name = name

        gif_db.put({
           'name': name,
           'category': 'disappointed',
           'thumbnail': thumb_name
        })

    for f_obj in funny_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)

        if ext == '.mp4':
            thumb_name = f_obj.filename.replace(ext, '.jpg')
            data = funny_thumbs_map[thumb_name]
            thumb_name = name.replace(ext, '.jpg')
            gif_drive.put(thumb_name, data)
        else:
            thumb_name = name

        gif_db.put({
           'name': name,
           'category': 'funny',
           'thumbnail': thumb_name
        })

    for f_obj in applause_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)

        if ext == '.mp4':
            thumb_name = f_obj.filename.replace(ext, '.jpg')
            data = applause_thumbs_map[thumb_name]
            thumb_name = name.replace(ext, '.jpg')
            gif_drive.put(thumb_name, data)
        else:
            thumb_name = name

        gif_db.put({
           'name': name,
           'category': 'applause',
           'thumbnail': thumb_name
        })

    for f_obj in sad_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)

        if ext == '.mp4':
            thumb_name = f_obj.filename.replace(ext, '.jpg')
            data = sad_thumbs_map[thumb_name]
            thumb_name = name.replace(ext, '.jpg')
            gif_drive.put(thumb_name, data)
        else:
            thumb_name = name

        gif_db.put({
           'name': name,
           'category': 'sad',
           'thumbnail': thumb_name
        })

    for f_obj in misc_files:
        if not f_obj.filename:
            continue
        ext = os.path.splitext(f_obj.filename)[-1]
        name = str(time()).replace('.', '') + ext
        gif_drive.put(name, f_obj.file)

        if ext == '.mp4':
            thumb_name = f_obj.filename.replace(ext, '.jpg')
            data = misc_thumbs_map[thumb_name]
            thumb_name = name.replace(ext, '.jpg')
            gif_drive.put(thumb_name, data)
        else:
            thumb_name = name

        gif_db.put({
           'name': name,
           'category': 'misc',
           'thumbnail': thumb_name
        })

    return {'status': status}


@router.get('/v1/gifs')
def get_gifs():
    gifs_map_model = {
        'happy': {'items': [], 'last': ""},
        'disappointed': {'items': [], 'last': ""},
        'funny': {'items': [], 'last': ""},
        'applause': {'items': [], 'last': ""},
        'sad': {'items': [], 'last': ""},
        'misc': {'items': [], 'last': ""}
    }

    gifs_map = {}

    for key in gifs_map_model:
        resp = gif_db.fetch({'category': key}, limit=8)
        items = []
        if resp.items:

            gifs_map[key] = {'items': [], 'last': ""}

            for row in resp.items:
                items.append(row['thumbnail'])

            gifs_map[key]['items'] = items
            gifs_map[key]['last'] = resp.last

    return gifs_map


@router.get('/v1/{name}')
def get_media(name: str):
    ext = os.path.splitext(name)[-1]
    mime = mime_map[ext]
    resp = gif_drive.get(name)
    return StreamingResponse(resp.iter_chunks(1024), media_type=mime)
