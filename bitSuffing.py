def bitStuffing(str):
    c = 0
    stuffedBit = ""
    for bit in str:
        stuffedBit += bit
        if bit == '1':
            c = c + 1
        else:
            c = 0
        if c == 5:
            stuffedBit += '0'
            c = 0
    return stuffedBit

def main():
    str = input("\nEnter the bit string to be stuffed: ")
    stuffedBit = bitStuffing(str)
    print("\nAfter stuffing bit string is: " + stuffedBit + "\n")

main()