#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> zfunction (string s, int n) {
	vector<int> z (n);
	int left = 0;
	int right = 0;
	for (int i = 1; i < n; i++) {
			z[i] = max(0, min (right - i + 1, z[i - left]));
		while (i + z[i] < n && s[z[i]] == s[i + z[i]])
			z[i]++;
		if (i + z[i] - 1 > right){
			left = i;
			right = i + z[i] - 1;
		}
	}
	return z;
}

int main()
{
    string s;
    cin >> s;
    int n = s.length();
    vector<int> z = zfunction(s, n);
    for (int i = 1; i < n; i++){
        cout << z[i] << " ";
    }
    return 0;
}
