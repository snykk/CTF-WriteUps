#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

//gcc chall.c -m32 -fno-stack-protector -no-pie -o timguakurang1

void logo(){
  puts("██╗     ██╗███╗   ██╗███████╗");
  puts("██║     ██║████╗  ██║╚══███╔╝");
  puts("██║     ██║██╔██╗ ██║  ███╔╝ ");
  puts("██║     ██║██║╚██╗██║ ███╔╝  ");
  puts("███████╗██║██║ ╚████║███████╗");
  puts("╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝");
}

void setup(){
  setvbuf(stdin,0,2,0);
  setvbuf(stdout,0,2,0);
}

int main(int argc, char **argv)
{
  setup();
  logo();
  volatile int modified;
  char buffer[64];

  modified = 0;
  printf("Input some text: ");
  gets(buffer);

  if(modified == 0xffffffff) {
    system("cat flag");
  } else {
    printf("Try again?\n");
  }

  return 0;
}