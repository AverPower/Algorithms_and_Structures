#include <iostream>
#include <vector> 
#include <cmath>

using namespace std;

const long INF = 1e9;

int main(){
    long n;
    cin >> n;
    vector<vector<long>> vertex(n, vector<long>(2));
    vector<bool> used(n);
    for (long i = 0 ; i < n; i++){
        cin >> vertex[i][0] >> vertex[i][1];
    }
    vector<long> w(n, INF);
    w[0] = 0;
    for (long i = 0; i < n; i++) {
    	long v = -1;
    	for (long j = 0; j < n; j++){
    		if (!used[j] && (v == -1 || w[j] < w[v])){
    			v = j;
    		}
    	}
    	used[v] = true;
    	for (long u = 0; u < n; u++){
    	    long dist;
    	    if (u != v and !used[u]){
        	    dist = (vertex[v][0] - vertex[u][0]) * (vertex[v][0] - vertex[u][0]) + (vertex[v][1] - vertex[u][1]) * (vertex[v][1] - vertex[u][1]);
        		if (dist < w[u]) {
        			w[u] = dist;
    	        }
	        }
	    }
	}
    
    double result = 0;
    for (int j = 0; j < n; j++){
        result += sqrt(w[j]);
    }
    cout << result;
}
