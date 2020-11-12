#include <iostream>
#include <cmath>
#include <string.h>

using namespace std;

long long INF = 1e-18 + 1;

class SegmentTree{
	public:
		long long * tree;
		long long * plus, *sets;
		unsigned long size;
		
		SegmentTree(long long *a, unsigned long n){
			
			unsigned long k;
			k = nearest_k(n);
			
			size = pow(2, k) - 1;
			unsigned long s = pow(2, k + 1) - 1;
			tree = new long long[s];
			unsigned long x = size + 1;
			for (unsigned long i = 0; i < s; i++){
				tree[i] = INF;
			}
			for (unsigned long i = 0; i < n; i++){
				tree[i + x - 1] = a[i];
			}
			for (int v = x - 2; v >=0; v--){
				tree[v] = min(tree[2 * v + 1], tree[2 * v + 2]);
			}
			
			plus = new long long[s];
			sets = new long long[s];
			for (unsigned long i = 0; i < s; i++){
				plus[i] = 0;
			}
			for (unsigned long i = 0; i < s; i++){
				sets[i] = INF;
			}
		}
		
		unsigned long nearest_k(unsigned long n){
			unsigned long k = 0;
			while (pow(2, k) < n){
				k += 1;
			}
			return k;
		} 
		
		long long rmq(unsigned long v, unsigned long l, unsigned long r, unsigned long a, unsigned long b){
			push(v, l, r);
			if (l > b || r < a){
				return INF;
			}
			if (l >= a and r <= b){
				return get(v);
			}
			unsigned long m = (l + r) / 2;
			return min(rmq(2 * v + 1, l, m, a, b), rmq(2 * v + 2, m + 1, r, a, b));
		}
		
		void add(unsigned long v, unsigned long l, unsigned long r, unsigned long a, unsigned long b, long long x){
			push(v, l, r);
			if (l > b || r < a){
				return;
			}
			if (l >= a and r <= b){
				plus[v] += x;
				return;
			}
			unsigned long m = (l + r) / 2;
			add(2 * v + 1, l, m, a, b, x);
			add(2 * v + 2, m + 1, r, a, b, x);
			tree[v] = min(get(2 * v + 1), get(2 * v + 2));
		}
		
		void set(unsigned long v, unsigned long l, unsigned long r, unsigned long a, unsigned long b, long long x){
			push(v, l, r);
			if (l > b || r < a){
				return;
			}
			if (l >= a and r <= b){
				sets[v] = x;
				return;
			}
			unsigned long m = (l + r) / 2;
			set(2 * v + 1, l, m, a, b, x);
			set(2 * v + 2, m + 1, r, a, b, x);
			tree[v] = min(get(2 * v + 1), get(2 * v + 2));
		}
		
		void push(unsigned long v, unsigned long l, unsigned long r){
			if (l == r){
				if (sets[v] != INF){
					tree[v] = sets[v] + plus[v];
					sets[v] = INF;
					plus[v] = 0;
				}
				else{
					tree[v] += plus[v];
					plus[v] = 0;
				}
			}
			else{
				if (sets[v] != INF){
					sets[2 * v + 1] = sets[v];
					sets[2 * v + 2] = sets[v];
					plus[2 * v + 1] = plus[v];
					plus[2 * v + 2] = plus[v];
				}
				else{
					plus[2 * v + 1] += plus[v];
					plus[2 * v + 2] += plus[v];
				}
				unsigned long m = (l + r) / 2;
				tree[v] = min(get(2 * v + 1), get(2 * v + 2));
				plus[v] = 0;
				sets[v] = INF;
			}
		}
		
		long long get(unsigned long v){
			if (sets[v] != INF){
				return sets[v] + plus[v];;
			}
			else{
				return tree[v] + plus[v]; 
			}
		}
};


int main()
{
    unsigned long n;
    cin >> n;
    long long *a;
    a = new long long[n];
    
    for (unsigned long i = 0; i < n; i++){
        cin >> a[i];
    }
    SegmentTree segtree = SegmentTree(a, n);
    char oper[3];
    unsigned long l, r;
    long long x;
    while(cin >> oper) {
        if (! strcmp(oper, "min")){
            cin >> l >> r;
            cout << segtree.rmq(0, 0, segtree.size, l - 1, r - 1) << endl; 
        }
        else {
            cin >> l >> r >> x;
            if (! strcmp(oper, "set")){
                segtree.set(0, 0, segtree.size, l - 1 , r - 1, x);
            }
            else{
                segtree.add(0, 0, segtree.size, l - 1, r - 1, x);
            }
        }
    }

    return 0;
}

