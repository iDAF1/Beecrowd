#include <stdio.h>

int main(){
    char name[100];
    double fxslr, tsld, total;
    scanf("%s", name);
    scanf("%lf", &fxslr);
    scanf("%lf", &tsld);
    total = fxslr + (tsld * 0.15);
    printf("TOTAL = R$ %.2lf\n", total);
    return 0;
}
