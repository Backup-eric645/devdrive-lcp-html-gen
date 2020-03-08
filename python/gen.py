import sys
if sys.version_info[0] < 3:
    from urllib       import quote
else:
    from urllib.parse import quote
def generate(text):
    return '<iframe src="http://devdrive.org/lcpdisp?lcptext=' + quote(text) + '"></iframe>'
