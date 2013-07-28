# coding=utf8

import getopt
import sys
import md5
import os
from md5_parser import *

output = "./file_md5.data"

opts, args = getopt.getopt( sys.argv[1:], None, ["output="] )

for k, v in opts:
    if k == '--output':
        output = v

folders = args

if len(folders)==0:
    print "No folders specified! Quiting..."
    exit(1)

# 这里保存md5码到文件列表的映射
path_to_md5 = {}

Parse( output, path_to_md5 )
to = open( output, "w")

def Make( folder, to_dic ):
    new_count = 0
    old_count = 0
    for root, dirs, files in os.walk( folder ):
        for f in files:
            path = os.path.join( root, f )
            
            abspath =os.path.abspath(path)
            print path[-60:]
            if to_dic.has_key( abspath ):
                old_count += 1
                hash = to_dic[abspath]  # @ReservedAssignment
            else:
                hash = FileMd5( path )
                to_dic[abspath] = hash
                new_count += 1
                
            to.write( "%s=%s\n"%(abspath,hash) )
    return new_count, old_count

new_count = 0
old_count = 0
for folder in folders:
    n, o = Make( folder, path_to_md5 )
    new_count += n
    old_count += o

to.close()

print "New file count:", new_count
print "Old file count:", old_count

