with open("binary", 'bw') as bin_file:  # b for binary, and w for write
    for i in range(17):
        bin_file.write(bytes([i]))  # b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n'

with open("binary", 'br') as bin_file:  # b for binary, and r for read
    for b in bin_file:
        print(b)  # b'\x0b\x0c\r\x0e\x0f\x10'

a = 65534  # FF EE
b = 65535  # FF FF
c = 65536  # 00 01 00 00
x = 2998302  # 02 2D C0 1E

with open("binary2", 'bw') as binFile:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))

with open("binary2", 'br') as binFile:
    e = int.from_bytes(binFile.read(2), 'big')
    print(e)
    f = int.from_bytes(binFile.read(2), 'big')
    print(f)
    g = int.from_bytes(binFile.read(4), 'big')
    print(g)
    h = int.from_bytes(binFile.read(4), 'big')
    print(h)
    i = int.from_bytes(binFile.read(4), 'big')
    print(i)
