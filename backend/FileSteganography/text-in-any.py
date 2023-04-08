import os

TEMP = "ImageSteganography/assets/temp.txt"

def embed(host,secret):
    with open(TEMP,"w") as f:
        f.write(secret)
    os.system(f'copy "{TEMP}+{host}"+"{TEMP}"')

if __name__=="__main__":
    print(":: Welcome to Steganography ::")
    img = input("Enter image name(with extension) : ")
    data = input("Enter data to be encoded : ")
    embed(host=img,secret=data)