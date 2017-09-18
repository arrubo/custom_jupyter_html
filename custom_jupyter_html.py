# python clean_jupyter_html.py
import os
import argparse
import re

parser = argparse.ArgumentParser(description='Extract clean document from Jupyter html')
parser.add_argument('-fi', metavar='--file_in' , help='file of Jupyter downloaded html file')
parser.add_argument('-fo', metavar='--file_out', help='file for cleaned html file')
parser.add_argument('-js', metavar='--file_js' , help='file with javascript to insert', default='custom.js', type=str,)
parser.add_argument('-f', metavar=' --force'   , help='force overwrite file_out if is the case', default=True, type=bool, choices=[True,False])
args = parser.parse_args()

def check_inputs(args):
    if not vars(args)['fi']:
        raise Exception("** ERROR: Make sure you provide the parameter -fi. (See --help)")
    match = re.match("^([^.]+)\.{1}([^.]+)$|^(.*)\.{1}([^.]+)\.{1}([^.]+)$", vars(args)['fi'])
    try:
        filename = match.group(1) or match.group(3)
    except:
        raise Exception("** ERROR: Make sure you provide a valid filename for the parameter -fi. (See --help)")
    version = match.group(4) or "0"
    extension = match.group(2) or match.group(5)
    if not version.isdigit():
        filename=filename+"."+version
        version="000"
    else:
        version= "{version}".format(version=version.zfill(3))
    if not vars(args)['fo']:
        vars(args)['fo']= filename+".cleaned."+version+"."+extension
    while os.path.isfile(vars(args)['fo']):
        version = str(int(version) + 1)
        version = "{version}".format(version=version.zfill(3))
        vars(args)['fo']= filename+".cleaned."+version+"."+extension

def insert_js(args):
    with open(vars(args)['fi'], "r") as file_in:
        html_in= file_in.read()
    with open(vars(args)['js'], "r") as file_js:
        js= file_js.read()
    html_out= html_in.replace("</html>","<script>"+js+"</script></html>")
    with open(vars(args)['fo'], "w+") as file_out:
        file_out.write(html_out)

if __name__ == '__main__':
    check_inputs(args)
    insert_js(args)