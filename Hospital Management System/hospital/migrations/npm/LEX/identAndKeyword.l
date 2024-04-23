%{
%}

%%
if|else|while|return|for|int {
    printf("%s is a keyword.\n",yytext);
}
[a-zA-Z_][a-zA-Z0-9_]* { 
    printf("%s is a indentifier.\n",yytext);
}
%%

int main(){
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}