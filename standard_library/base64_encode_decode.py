import base64

#Encoding a string using Base64
string_to_decode="Hello,world!"
encoded_string=base64.b64encode(string_to_decode.encode("utf-8"))
print(encoded_string)#b 'SGVsbG8ssakdfsjdf==/n'
#transfer ecoded string over network

#Decoding a Base64-encoded string
decoded_string=base64.b64decode(encoded_string.decode('utf-8'))
print(decoded_string)#'Hello,world'