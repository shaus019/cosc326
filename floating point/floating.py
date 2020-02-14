import os
import struct
def parseIBMfloating(inputpath,inputprecision):
    results = []
    expectedLength = 32 if inputprecision=="single" else 64
    with open(inputpath,"r") as file:
        nums = file.readlines()
        for oneNum in nums:
            if(len(oneNum)!=expectedLength):
                pass
            oneNum = oneNum.strip("\n").replace(" ","")
            if(oneNum[0]=="1"):
                sign = -1
            elif(oneNum[0]=="0"):
                sign = 1
            exponent = oneNum[1:8]
            fraction = oneNum[8:]
            expodigit = bin_to_digit(exponent) - 64
            afterdigit = bin_to_digit_after(fraction)
            result = (afterdigit*(16**expodigit)) * sign
            results.append(result)
    return results

def writeIEEE(outputpath,results,outputprecision):
    with open(outputpath,"w") as out_file:
        for data in results:
            if(outputprecision=="single"):
                packed = struct.pack('>f',data).encode('hex')
                bin = "{0:08b}".format(int(packed,16))
                if(bin[0]=="0"):
                    if(int(bin)==0):
                        bin = "0"*32
                elif(bin[0]=="1"):
                    if(int(bin[1:])==0):
                        bin = "1"+"0"*31
                if(len(bin)==31):
                    out_file.write("0"+bin+"\n")
                else:
                    out_file.write(bin+"\n")
            elif(outputprecision=="double"):
                packed = struct.pack('>d',data).encode('hex')
                bin = "{0:08b}".format(int(packed,16))
                if(bin[0]=="0"):
                    if(int(bin)==0):
                        bin = "0"*64
                elif(bin[0]=="1"):
                    if(int(bin[1:])==0):
                        bin = "1"+"0"*63
                if(len(bin)==63):
                    out_file.write("0"+bin+"\n")
                else:
                    out_file.write(bin+"\n")
def bin_to_digit(binary):
    digit = 0
    for i,num in enumerate(reversed(binary)):
        digit += 2**(i) * int(num)
    return digit
def bin_to_digit_after(binary):
    digit = 0
    for i,num in enumerate(binary):
        digit += 2**(-(i+1)) * int(num)
    return digit

def insert_dot(fraction,pos):
    return fraction[:pos], fraction[pos:].strip("0")
"""
#testing
def test():
    oneNum = "01000010011101101010000000000000"
    oneNum = "01111111111111111111111111111111"
    if(oneNum[0]=="1"):
        sign = -1
    elif(oneNum[0]=="0"):
        sign = 1
    exponent = oneNum[1:8]
    fraction = oneNum[8:]
    expodigit = bin_to_digit(exponent) - 64
    afterdigit = bin_to_digit_after(fraction)
    result = (afterdigit*(16**expodigit)) * sign
    print(result)
test()
"""
