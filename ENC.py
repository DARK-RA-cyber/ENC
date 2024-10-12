# -*- coding:utf8 -*-
#--------------------------------------------------
#--------CODE BY ASRAFUL--------
#--------------------------------------------------
#      \033[1;30m    ➤ Black
#      \033[1;31m    ➤ Red
#      \033[1;32m    ➤ Green
#      \033[1;33m    ➤ Yellow
#      \033[1;34m    ➤ Blue
#      \033[1;35m    ➤ Purple (pink)
#      \033[1;36m    ➤ Cyan (sky)
#      \033[1;37m    ➤ White

# Import Modules
import os
import sys
import zlib
import time
import base64
import marshal
import py_compile

# Select raw_input() or input()
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\n [×] Your Python Version is not Supported!")

# Encoding
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))
note = "#--------------------------------------------------\n#--------HEY BRO WASSUP--------\n#--------------------------------------------------\n#Encoder : DARK-RA\n#Facebook : MUHAMMAD RONI AKANDO\n#GitHub : DARK-RA-cyber\n#Telegram : DARK_RA12\n#--------------------------------------------------\n\n\n"

def banner(): # Program Banner
    
    print("       \033[1;31m┃\033[47m\033[1;46m  DEVELOPER    ➤ DARK-RA   \033[40m\033[00m\x1b[1;91m┃")
    print("       \033[1;31m┃\033[47m\033[1;46m  GITHUB    ➤ DARK-RA-cyber\033[40m\033[00m\x1b[1;91m┃")
    print("       \033[1;31m┃\033[47m\033[1;46m  𝚃𝚘𝚘𝚕 𝚃𝚢𝚙𝚎 ➤ 𝙿𝚈𝚃𝙷𝙾𝙽 𝙴𝙽𝙲𝙾𝙳𝙴𝚁  \033[40m\033[00m\x1b[1;91m┃")
    print("       \033[1;31m┃\033[47m\033[1;46m  𝚅𝚎𝚛𝚜𝚒𝚘𝚗   ➤ VOLUME MAX        \033[40m\033[00m\x1b[1;91m┃")

def menu(): # Program Menu

    print('       \033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m01\033[1;31m] \033[1;36mEncode Marshal          \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m02\033[1;31m] \033[1;36mEncode Zlib             \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m03\033[1;31m] \033[1;36mEncode Base16           \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m04\033[1;31m] \033[1;36mEncode Base32           \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m05\033[1;31m] \033[1;36mEncode Base64           \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m06\033[1;31m] \033[1;36mEncode Zlib,Base16      \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m07\033[1;31m] \033[1;36mEncode Zlib,Base32      \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m08\033[1;31m] \033[1;36mEncode Zlib,Base64      \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m09\033[1;31m] \033[1;36mEncode Marshal,Zlib     \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m10\033[1;31m] \033[1;36mEncode Marshal,Base16   \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m11\033[1;31m] \033[1;36mEncode Marshal,Base32   \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m12\033[1;31m] \033[1;36mEncode Marshal,Base64   \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m13\033[1;31m] \033[1;36mEncode Marshal,Zlib,B16 \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m14\033[1;31m] \033[1;36mEncode Marshal,Zlib,B32 \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m15\033[1;31m] \033[1;36mEncode Marshal,Zlib,B64 \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m16\033[1;31m] \033[1;36mEncode Randomly         \033[1;32m┃")
    print("       \033[1;32m┃ \033[1;31m[\033[1;36m17\033[1;31m] \033[1;31mExit Program            \033[1;32m┃")
    print('       \033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n')
class FileSize: # Gets the File Size
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print("   \033[1;33m[/] Encoded File Size : %s\n" % self.datas(dts))
# FileSize('rec.py')

# Encode Menu
def Encode(option,data,output):
    loop = int(eval(_input % "       \033[1;32m[+] Encode Count : "))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        sys.exit("\n Invalid Option!")
    
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()

# Special Encode
def SEncode(data,output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output,output)

# Main Menu
def MainMenu():
    try:
        os.system('clear') # os.system('cls')
        banner()
        menu()
        try:
            option = int(eval(_input % "       \033[1;33m[+] Option : "))
        except ValueError:
            sys.exit("\n       \033[1;31m[×] Invalid Option !")
        
        if option > 0 and option <= 17:
            if option == 17:
                time.sleep(3)
                sys.exit("\n  \033[1;36m- Thanks For Using  Tool")
            os.system('clear') # os.system('cls')
            banner()
        else:
            sys.exit('\n       \033[1;31m[×] Invalid Option !')
        try:
            file = eval(_input % "       \033[1;33m[+] File Path : ")
            data = open(file).read()
        except IOError:
            sys.exit("\n\033[1;31m      [×] File Not Found!")
        
        output = file.lower().replace('.py', '') + '_SAXX.py'
        if option == 16:
            SEncode(data,output)
        else:
            Encode(option,data,output)
        print("\n \033[1;32m  [√] Successfully Encrypted %s" % file)
        print("\033[1;36m   [√] Saved as %s" % output)
        print("\033[1;33m - Thanks For Using ASRAFUL AHMED'S Tool")
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    MainMenu()
    