#include <stdio.h>

int arr[1100000];

int find(int x, int size) {
    int low = 0, high = size - 1;
    int mid, occ = 0;
    while(low <= high) {
        mid = (low + high) / 2;
        if(arr[mid] == x) {
            occ = 1;
            break;
        }
        else if(arr[mid] < x) {
            low = mid + 1;
        }
        else high = mid - 1;
    }
    if(occ > 0) {
        low = mid - 1;
        while(low >= 0 && arr[low] == x) {
            low--;
            occ++;
        }
        high = mid + 1;
        while(high < size && arr[high] == x) {
            high++;
            occ++;
        }
    }
    return occ;
}

int main() {
    int n, m, i, k, x;
    while(scanf("%d", &n) != EOF) {
        for(i = 0; i < n; i++) {
            scanf("%d", &k);
            arr[i] = k;
        }
        scanf("%d", &m);
        for(i = 0; i < m; i++) {
            scanf("%d", &x);
            k = find(x, n);
            printf("%d\n", k);
        }
    }
}
