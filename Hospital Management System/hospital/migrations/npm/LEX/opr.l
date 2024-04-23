%{
%}

%%
[-+*/<>!&|]+ { printf("%s is an operator.\n",yytext); }
%%

int main(){
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}