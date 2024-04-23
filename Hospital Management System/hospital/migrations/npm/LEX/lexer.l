%{
#include <stdio.h>
%}

%%
[a-zA-Z]+ { printf("Word: %s\n",yytext); }
%%

int main(){
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}
