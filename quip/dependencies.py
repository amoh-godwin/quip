import os

from deta import Deta


deta = Deta()

gif_drive = deta.Drive('gifs')
gif_db = deta.Base('gifs')
