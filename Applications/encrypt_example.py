import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(key, filename):
    chunksize = 64 *1024
    outputFile = "(encrypted)"+ filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = ''

    for i in range(16):
        IV+= chr(random.randint(0,0xFF))

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with opne(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize)
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) ==0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' '*(16-(len(chunck)% 16))

                outfile.write(encryptor.encrypt(chunck))

def decrypt(key, filename):
    chuncksize = 64 * 1024
    outputFile = filename[11:]
    with open(filename, 'rb')as infile:
        filesize = long(infile.read(16))
        IV= infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)
        with open(outputFile, 'wb')as outfile:
            while True:
                chunck = infile.read(chuncksize)
                if len(chunck) == 0:
                    break
                outfile.write(decryptor.decrypt(chunck))
            outfile.truncate(filesize)

def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()

def Main():
    choice = input('would you like to (E)ncrypt or (D)encrypt?:')
    if choice =='E':
        filename = input('File to encrypt')
        password = input('password')
        encrypt(getKey(password), filename)
        print('Done')

    elif choice == 'D':
        file = input('File to decrypt: ')
        password = input('Password: ')
        if password != password:
            print('wrong password')
        decrypt(getKey(password), filename)
        print('Done')

    else:
        print('No option selected')

if __name__ == '__main__':
    Main()
