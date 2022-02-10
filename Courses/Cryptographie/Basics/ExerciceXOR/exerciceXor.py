# exercice inspired from https://cryptohack.org/courses/intro/xor1/

from operator import xor

key1       = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
key2Xor3   = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flagXor132 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

val = hex(xor(xor(int.from_bytes(flagXor132, "big"),int.from_bytes(key2Xor3, "big")),int.from_bytes(key1, "big")))

print (val)
print(type(val))
print(bytes.fromhex(val[2:]))