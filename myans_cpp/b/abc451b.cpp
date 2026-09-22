#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,s,n) for(int i=(s);i<(s)+(int)(n);i++)
using ll=long long;

int main() {
    int n,m;
    cin >> n >> m;

    // n行のリストを0で初期化
    vector<int> ans(m,0);
    // n*n行のリストを0で初期化
    // vector<vector<int>> ans(n, vector<int>(n, 0));

    rep(i,n){
        int a,b;
        cin >> a >> b;
        a-=1;
        b-=1;
        ans[a]-=1;
        ans[b]+=1;
    }

    rep(i,m){
        cout << ans[i] << endl;
    }
}