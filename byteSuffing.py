def ByteStuffing(str,flag):
    stuffedString = ""
    stuffedString += flag
    for byte in str:
        if byte == flag:
            stuffedString += flag
            stuffedString += byte
        else:
            stuffedString += byte
    stuffedString += flag
    return stuffedString

def main():
    str = input("Enter the byte string to be stuffed: ")
    flag = input("Enter a the flag element: ")
    stuffedString = ByteStuffing(str,flag)
    print("After stuffing byte string is: ", stuffedString)

main()
