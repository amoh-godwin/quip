from typing import List

from fastapi import APIRouter, File, UploadFile, Form

# from dependencies import gif_drive


router = APIRouter(prefix='/api/gif_access')


@router.get('/v1/uploader')
def front_upload(
    category: str = Form(...),
    files: List[UploadFile] = File(...)
    ):
    return {'hello': [len(file) for file in files]}
