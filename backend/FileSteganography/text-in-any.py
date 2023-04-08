import os

matchkey = "C37DA957D83D607956789910AA4096C43734A220"
shellscript = 'backend/FileSteganography/extract.sh'
tempfile = "temp.dat"

def embed(host,secret,result):
    temp = list(host.split("."))
    temp[-1] = 'txt'
    TEMP = ".".join(temp)
    secret = matchkey+secret
    with open(TEMP,"w") as f:
        f.write(secret)
    os.system(f'cat "{host}" > {result}')
    os.system(f'cat "{TEMP}" >> {result}')
    

def extract(file):
    os.system(f'cat "{file}" > {tempfile}')
    os.system(f"{shellscript} {tempfile}")
    os.system(f"{shellscript} {tempfile}")
    x = ""
    with open('temp.dat','r') as f:
        x = f.read()
        print(x)
    return x

if __name__=="__main__":
    a = int(input(":: Welcome to Steganography ::\n1. Encode\n2. Decode\n"))
    if (a == 1):
        host = input("Enter file name(with extension) : ")
        secret = input("Enter data to be encoded : ")
        output = input("Enter the name of new audio(with extension) : ")
        embed(host,secret,output)
    elif (a == 2):
        host = input("Enter audio file name(with extension) : ")
        print("Decoded Word : " + extract(host))
    else:
        raise Exception("Enter correct input")