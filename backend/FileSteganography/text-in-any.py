import os

def embed(host,secret,result):
    temp = list(host.split("."))
    temp[-1] = 'txt'
    TEMP = ".".join(temp)
    with open(TEMP,"w") as f:
        f.write(secret)
    os.system(f'cat "{host}" > {result}')
    os.system(f'cat "{TEMP}" >> {result}')

if __name__=="__main__":
    print(":: Welcome to Steganography ::")
    img = input("Enter image name(with extension) : ")
    data = input("Enter data to be encoded : ")
    result = input("Enter the name of new image(with extension) : ")
    embed(host=img,secret=data,result=result)