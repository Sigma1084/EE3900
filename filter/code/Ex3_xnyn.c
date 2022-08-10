#include <stdio.h>
#include <stdlib.h>

int main() {
    float x[] = { 1.0, 2.0, 3.0, 4.0, 2.0, 1.0 };
    const int xLen = sizeof(x) / sizeof(float);

    const int k = 20;
    float y[k];

    y[0] = x[0]; y[1] = -0.5 * y[0] + x[1];

    for (int n=2; n<k; n++) {
        if (n < xLen) y[n] = -0.5 * y[n - 1] + x[n] + x[n - 2];
        else if (n+2 < xLen) y[n] = -0.5 * y[n - 1] + x[n - 2];
        else y[n] = -0.5 * y[n - 1];
    }

    FILE *fp = fopen("Ex3_output.txt", "w");

    for (int n=0; n<k; n++) fprintf(fp, "%f ", y[n]);
    fprintf(fp, "\n");
}
