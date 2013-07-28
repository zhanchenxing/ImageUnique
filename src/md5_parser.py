import os
import md5

def FileMd5( path ):
    m = md5.new()
    m.update( open(path, "rb").read() )
    return m.hexdigest()

def Parse( data_file, to ):
    if not os.path.isfile(data_file):
        return
    for line in open(data_file).readlines():
        line = line.strip('\n\r \t')
        path, hash = line.split('=')
        to[path] = hash