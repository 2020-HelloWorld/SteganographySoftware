# wave module comes with standard python installation
import wave
from os import path
from pydub import AudioSegment

temp = "FileSteganography/assets/result.wav"

def embed(infile: str, message: str, outfile: str):
    # convert mp3 file to wav file
    try:
        sound = AudioSegment.from_mp3(infile)
    except Exception as e:
        print(e)
        return
    
    sound.export(temp, format="wav")

    song = wave.open(temp, mode='rb')
    # Read frames and convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
    message = message + int((len(frame_bytes) - (len(message) * 8 * 8)) / 8) * '#'
    # Convert text to bit array
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in message])))

    # Replace LSB of each byte of the audio data by one bit from the text bit array
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)

    # Write bytes to a new wave audio file
    with wave.open(outfile, 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()


def extract(file: str):
    """This function takes the filepath and decodes the hidden data and returns it"""
    song = wave.open(file, mode='rb')
    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    # Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    # Convert byte array back to string
    message = "".join(chr(int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
    # Cut off at the filler characters
    decoded = message.split("###")[0]
    song.close()
    return decoded

# Main Function
def main():
    a = int(input(":: Welcome to Steganography ::\n1. Encode\n2. Decode\n"))
    if (a == 1):
        host = input("Enter audio file name(with extension) : ")
        secret = input("Enter data to be encoded : ")
        output = input("Enter the name of new audio(with extension) : ")
        embed(host,secret,output)
    elif (a == 2):
        host = input("Enter audio file name(with extension) : ")
        print("Decoded Word : " + extract())
    else:
        raise Exception("Enter correct input")

# Driver Code
if __name__ == '__main__' :   
    main()