%{
%}

%%
[AEIOUaeiou]+ {
    printf("%s is a vowel.",yytext);
}
. {
    printf("%s is a consonant.",yytext);
}
%%

int main(){
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}