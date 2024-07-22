#!/usr/bin/python3

def validUTF8(data: list):
    try:
        print(data)
        data_bytes = bytes(data)
        binary_data = [bin(i) for i in data]
        binary_back = [format(i, "08b") for i in data_bytes]
        print("binary rep: ", type(binary_data[0]), binary_data)
        print("binary_back rep: ", type(binary_back[0]), binary_back)
        print("------> ", int((binary_data[0]), 2))
        print("Byte data: ", type(data_bytes), data_bytes)

        data_decode = data_bytes.decode("utf-8")
        print("Data decoded :", data_decode)
    except Exception as e:
        print(e)

    return True


print(int("10000000", 2))
print(format(128, "08b"))
data = [0xc0, 0xaf]
data_conv = [int(str(i), 16) for (i) in data]
print(data_conv)
print(bytes(data_conv))
data_conv = [bin(i) for i in data_conv]

print(data_conv)
