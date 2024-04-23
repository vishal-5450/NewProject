%{
    #include<stdio.h>
    #include<string.h>

    char largestWord[100]="";
%}

%%
[A-Za-z]+ {
    if(strlen(yytext)>strlen(largestWord)){
        strcpy(largestWord,yytext);
    }
    printf("Largest Word: %s",largestWord);
}
%%

int main(){
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}