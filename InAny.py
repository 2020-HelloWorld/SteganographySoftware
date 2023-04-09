import os
from flask import current_app

matchkey = "C37DA957D83D607956789910AA4096C43734A220"
shellscript = '/home/gb/SteganographySoftware/extract.sh'

def embed(host,secret,result):
    secret = matchkey+secret
    with open("temp.dat","w") as f:
        f.write(secret)
    os.system(f'cat "{host}" > {result}')
    os.system(f'cat "temp.dat" >> {result}')
    os.system('rm "temp.dat"')
    return result
    
def extract(file,type):
    temp = list(file.split("."))
    temp[-1] = type
    output = ".".join(temp)
    os.system(f'cat "{file}" > "temp.dat"')
    os.system(f'{shellscript} "temp.dat"')
    os.system(f'cat "temp.dat" > "{output}"')
    os.system('rm "temp.dat"')
    return output #Returning file name
    

if __name__=="__main__":
    #Write test cases
    embed("/home/gb/SteganographySoftware/test.jpeg","Welcome to stegano")