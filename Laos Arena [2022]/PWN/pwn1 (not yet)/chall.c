#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

//gcc chall.c -fno-stack-protector -no-pie -o yangfokus


char flag[64];

void logo(){
  puts("██╗     ██╗███╗   ██╗███████╗");
  puts("██║     ██║████╗  ██║╚══███╔╝");
  puts("██║     ██║██╔██╗ ██║  ███╔╝ ");
  puts("██║     ██║██║╚██╗██║ ███╔╝  ");
  puts("███████╗██║██║ ╚████║███████╗");
  puts("╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝");
}

void alert(){
  puts("------------------- ALERT -------------------");
  puts("Yang mau serius di CSI tim gua kurang 1");
  puts("Tolong hub saya di discord Linz#7046");
  puts("------------------- THANKS -------------------");
  printf("\n");
}

void setup(){
  setvbuf(stdin,0,2,0);
  setvbuf(stdout,0,2,0);
  FILE *fp = fopen("flag","r");
  if(fp == NULL){
    printf("No file flag\n");
    exit(0);
  }
  fgets(flag,60,fp);
}


int main(int argc, char **argv)
{
  setup();
  logo();
  alert();
  char buffer[64];
  printf("Jangan lupa hub saya: ");
  gets(buffer);
  return 0;
}


int linz_here(){
  printf("%s\n", flag);
}