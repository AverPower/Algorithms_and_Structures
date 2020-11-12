#include <iostream>
#include <conio.h>
#include <algorithm>

using namespace std;

unsigned int N_1 = 65536;
long long N_2 = 1073741824;


unsigned long long rsq(unsigned int l, unsigned int r, unsigned long long *mas){
    if (l == 0){
        return mas[r];
    }
    return mas[r] - mas[l - 1];
}

void count_sums(long long n, long long a_0, long long x, long long y, unsigned long long *sums){
    sums[0] = a_0;
    unsigned int a_prev = a_0;
    for (long long i = 1; i < n; i++){
        unsigned int temp;
        temp = x * a_prev + y;
        if (temp >= N_1) {
            temp = temp % N_1;
        }
        a_prev = temp;
        sums[i] = sums[i - 1] + temp;
    }
}
void count_c(long long n, long long m, long long z, long long t, long long b_0, unsigned int *c){
    long long b_prev = b_0;
    c[0] = b_0 % n;
    for (long long i = 1; i < 2 * m; i++){
        unsigned long long temp;
        temp = z * b_prev;
        if (temp >= N_2){
            temp = temp % N_2;
        }
        if (temp == 0 && t == -1){
            temp = N_2 - 1;
        }
        else{
            temp = (temp + t) % N_2;
        }
        b_prev = temp;
        c[i] = temp % n;
    }
}

int main()
{
    long long n, x, y, a_0, m, z, t, b_0;
    
    cin >> n >> x >> y >> a_0 >> m >> z >> t >> b_0;
    
    unsigned long long *sums;
    sums = new unsigned long long[n];
    count_sums(n, a_0, x, y, sums);

    unsigned int *c;
    c = new unsigned int[2 * m];
    count_c(n, m, z, t, b_0, c);

    unsigned long long res = 0;
    for (unsigned int i = 0; i < m; i++){
        unsigned int l, r;
        l = min(c[2 * i], c[2 * i + 1]);
        r = max(c[2 * i], c[2 * i + 1]);
        res += rsq(l, r, sums);
    }
    cout << res;
    return 0;
}
