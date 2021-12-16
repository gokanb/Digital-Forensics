import hashlib

def hash_file(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as open_file:
        buff_size = 1024
        buff = open_file.read(buff_size)
        
        while buff:
            sha256.update(buff)
            buff = open_file.read(buff_size)
            
    return sha256.hexdigest()