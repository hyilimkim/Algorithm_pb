from Pycrypto.Ciphter import AES
# 길이 32의 hex string을 받아 길이 16의 bytes object를 생성합니다.
# 대소문자는 상관 없습니다.
# bytes 대신 bytearray를 사용하면 바이트 값을 하나하나 수정할 수 있습니다. 문제 풀이에 도움이 될 수도..
key = bytes.fromhex('A0000000000000000000000000000000')
# 주어진 키를 이용해 AES object를 생성합니다.
# 키가 길이 16의 bytes/bytearray이면 AES128을 사용합니다.
cipher = AES.new(key, AES.MODE_ECB)
# cipher.encrypt와 decrypt 함수는 길이 16의 bytes를 받아 길이 16의 bytes를 생성합니다.
# (각각 암호화, 복호화)
# 같은 키로 암호화했다가 복호화하면 원래 데이터가 bytes 형태로 나옵니다.
data = bytes.fromhex('00112233445566778899AABBCCDDEEFF')
ciphertext = cipher.encrypt(data)
plaintext = cipher.decrypt(ciphertext)
assert data == plaintext
# bytes에서 hex로 만들려면 bytes.hex()를 사용합니다.
# 소문자를 주기 때문에 제출 형식에 맞추기 위해 .upper()가 필요합니다.
print(key.hex().upper())