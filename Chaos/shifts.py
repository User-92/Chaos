inStr = input('>>> ')
shift = 31
##outStr = ''.join([chr((ord(c)+shift)%256) for c in inStr])
outStr = ''.join([chr((ord(c)+shift+i)%256) for i,c in enumerate(inStr)])
print(outStr)