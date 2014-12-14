import subprocess
import os

# setup the path to extopenscad (aka implicitCAD)
cad_bin=os.path.expanduser('~/.cabal/bin/extopenscad')
# set the current input dir to this script file's dir
inp_dir = '.'
# set the output to a directory next to this script file
out_dir = './output'
# set the output file extension to .stl
out_type='.stl'

# make any paths relative (this probably needs work)
out_dir=os.path.abspath(out_dir)

if not os.path.isdir(inp_dir):
    inp_dir=os.path.abspath(os.path.join(
                 os.path.dirname(__file__), inp_dir
                                     )
                        )
# the -o option tells extopenscad to ouput a file to the subsequent path
o='-o'

try:
    os.makedirs(out_dir)
except OSError as e:
    # don't complain if the dir already exists
    if e.errno!=17:
        raise e

# go through each item in the input dir
for f in os.listdir(inp_dir):
    # if the item is a .escad file, process
    if '.escad' in f:
        # remove .escad from the filename
        n=f[0:f.index('.escad')]
        # join the output dir with the stripped file and the output filetype
        out= os.path.join(out_dir,
                          n + out_type
                         )
        # join the input directory and the current dir list item
        inp=os.path.join(inp_dir, f)
        # emit what we came up with for a command
        print cad_bin, o, out, inp
        # run the command
        p=subprocess.Popen([cad_bin, o, out, inp],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        # wait for the command's output
        s, e=p.communicate()
        # print the command's output
        print s
        print e
