from base64 import b64encode

encoded = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

test = bytearray.fromhex('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')

output = b64encode(test)

print(output)