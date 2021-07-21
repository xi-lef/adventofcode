// nasm -f elf64 23.asm && gcc 23.c 23.o -o 23asm && ./23asm
#include <stdio.h>

unsigned long simu();

// runtime: 138 mins lmao
int main() {
    unsigned long a = simu();
    printf("%lu\n", a);
}
