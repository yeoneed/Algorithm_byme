#include <stdio.h>
int main() {
    int n, num, max = -1000000, min = 100000;

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &num);
        if (min > num)
            min = num;
        if (max < num)
            max = num;
    }
    printf("%d %d", min, max);

    return 0;
}
