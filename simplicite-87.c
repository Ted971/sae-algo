#include<stdio.h>
#include<string.h>

char *effacer_espaces(char *str)
{
    for (int i=0; i < sizeof(str); i++)
    {
    if (str[i] == ' ' && str[i+1] == ' '){
      i = i+2;
    } else if (str[i] == ' ' && str[i+1] != ' '){
      str[i] = "\0";
      i ++;
    }}
    return str;
}