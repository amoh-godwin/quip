import os

from pyffmpeg import FFmpeg

ff = FFmpeg()


conts = os.listdir('../media')
os.chdir('../media')

for f in conts:
    if f.endswith('.mp4'):
        ff.convert(f, f.replace('.mp4', '.jpg'))
    print(f'converted: {f}')

print('Done converting files')
