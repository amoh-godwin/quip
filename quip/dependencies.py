
from deta import Deta


deta = Deta()

gif_drive = deta.drive('gifs')
gif_db = deta.Base('gifs')
