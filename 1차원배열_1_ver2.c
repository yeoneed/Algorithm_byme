//배열로 풀이(백준에선 컴파일 에러나서 안돌아감) 
#include <stdio.h>

int main() {
    int n, min = 1000000, max = -1000000;
    int num[10000];
    scanf_s("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf_s("%d", &num[i]);

        if (min > num[i])
            min = num[i];
        if (max < num[i])
            max = num[i];
    }
    printf("%d %d", min, max);
    return 0;
}
