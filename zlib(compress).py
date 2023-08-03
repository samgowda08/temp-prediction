'''
import zlib
s = b'This is a python programmming '
print(s,len(s))
t = zlib.compress(s)
print(t)
s1 = zlib.decompress(t)
print(s1)
print(zlib.crc32(s))
print(zlib.crc32(t))
print(zlib.crc32(s1))
'''
