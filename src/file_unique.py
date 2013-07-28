# coding=utf8

import getopt
import sys
import md5
import os
import shutil
from md5_parser import *

input = "./file_md5.data"

opts, args = getopt.getopt( sys.argv[1:], None, ["input="] )

for k, v in opts:
    if k == '--input':
        input = v

path_to_md5 = {}
Parse( input, path_to_md5 )

md5_to_path = {}
for path, md5 in path_to_md5.iteritems():
    md5_to_path.setdefault(md5, []).append(path)

to_remove = []

for md5, files in md5_to_path.iteritems():
    if len(files)>1:
        for path in files[1:]:
            if os.path.isfile(path):
                shutil.move( path, os.path.join( "F:\deleted_photo", path[path.rfind('\\')+1:] ) )
            to_remove.append( path )
        
        print '*'*79
        print md5
        for path in files:
            print "", path
        print

for abspath in to_remove:
    path_to_md5.pop(abspath)

to = open(input, "wb")
for abspath, hash in path_to_md5.iteritems():
    to.write( "%s=%s\n"%(abspath,hash) )
to.close()
