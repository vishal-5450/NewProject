%{

%}

%%
[0-9]+ {
    if(atoi(yytext) % 2 == 0){
        printf("%s is even.\n",yytext);
    }
    else{
        printf("%s is odd.\n",yytext);
    }
}
%%

int main(){
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}