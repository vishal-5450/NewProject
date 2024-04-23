%{
%}
%%
[0-9]+ {
    int n = atoi(yytext);
    int is_prime = 1;
    for(int i = 2;i <= n / 2;i++){
        if(n % i == 0){
            is_prime=0;
            break;
        }
    }
    if(is_prime && n>1){
        printf("%d is a Prime Number.",n);
    }else{
        printf("%d is not a Prime Number.",n);
    }
}
%%
int main() {
    yylex();
    return 0;
}
int yywrap(){
	return 1;
}
