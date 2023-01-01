# Encode and decode passwords using Base85.
import base64

# Original string:
a = 'nothing_2_do@me'
print(f'{a=}')

# String to bytes:
a_to_bytes = a.encode('utf8')
print(f'{a_to_bytes=}')

# Encode bytes using Base85:
a_encoded = base64.b85encode(a_to_bytes)
print(f'{a_encoded=}')

# Decode bytes using B85:
a_decoded = base64.b85decode(a_encoded)
print(f'{a_decoded=}')

# Bytes to string:
a_from_bytes = a_decoded.decode('utf-8')
print(f'{a_from_bytes=}')

# Check if original string is equal to restored one:
assert a == a_from_bytes, 'Error of encoding/decoding!'
