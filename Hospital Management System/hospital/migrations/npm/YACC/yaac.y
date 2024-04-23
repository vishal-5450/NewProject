%{
#include <stdio.h>
%}

%token NUM

%%

expr: NUM              { printf("%d ", $1); }
    | expr NUM        { printf("%d ", $2); }
    ;

%%

int main() {
    printf("Enter a sequence of numbers separated by spaces: ");
    yyparse();
    return 0;
}

int yylex() {
    int num;
    scanf("%d", &num);
    return num;
}

void yyerror(const char *msg) {
    fprintf(stderr, "Error: %s\n", msg);
}
