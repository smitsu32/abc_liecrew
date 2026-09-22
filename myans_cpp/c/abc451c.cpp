#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,s,n) for(int i=(s);i<(s)+(int)(n);i++)
using ll=long long;

int main() {
    int q;
    cin >> q;

    multiset<ll> ms;

    rep(i,q){
        int a,h;
        cin >> a >> h;
        
        if(a==1){
            ms.insert(h);
        }else{
            // 型を決めず返す
            auto it=ms.upper_bound(h);
            ms.erase(ms.begin(),it);
        }
        cout << ms.size() << endl;
    }
}