// compile: gcc -fno-stack-protector -no-pie basic_pwn.c -o ICEWALL_pwn_basic
#include <stdio.h>
#include <stdlib.h>

void flag() {
  char *cmd = "/bin/sh";
  char *args[] = {cmd, NULL};
  execve(cmd, args, NULL);
}

int main(int argc, char *argv[]) {
    char buf[0x10];

    puts("Welcome ICEWALL basic pwnable!!\nYou can enter up to 0x10 bytes.");
    read(0, buf, 0x50);

    puts(buf);

    return 0;
}