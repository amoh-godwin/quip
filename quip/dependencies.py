import os

from deta import Deta


key = os.environ['DETA_DEFAULT_KEY']


deta = Deta(key)

gif_drive = deta.Drive('gifs')
gif_db = deta.Base('gifs')
