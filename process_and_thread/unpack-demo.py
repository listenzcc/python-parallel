'''
File: unpack-demo.py
Author: Chuncheng Zhang
Purpose:
    Explain why the unpack method fails sometime.
    One possible reason is the 's' unpacking requires the array rather than single byte.
    The script provides an example
'''
# %%

from struct import pack, unpack

# %%

bytes = pack('ss', b'abcdefg', b'bcdef')
print('The pack:', bytes)

# %%
try:
    unpack('s', bytes[0])
except TypeError as err:
    print('\nIncorrect example:')
    print('Type error:\t', err)
    print('The bytes[0]:\t', bytes[0])

print('\nCorrect example:')
print('The unpack:\t', unpack('s', bytes[0:1]))
print('The unpack:\t', unpack('s', bytes[1:]))

print('\nDetail')
print('The bytes[0]:\t', bytes[0])
print('The bytes[0:1]:\t', bytes[0:1])


# %%
