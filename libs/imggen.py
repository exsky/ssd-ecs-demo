import os
from html2image import Html2Image

def gen(name):
    if not name:
        name = 'default'
    # Gen IMG
    hti = Html2Image()
    hti.output_path = 'tmp'
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
    outname = '{}.png'.format(name)
    hti.screenshot(
            html_file='pages/person.html',
            save_as=outname, size=(1000, 800))
    return outname
