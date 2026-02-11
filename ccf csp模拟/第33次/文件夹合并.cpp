/*
    Created by Pujx on 2024/5/8.
*/
#pragma GCC optimize(2, 3, "Ofast", "inline")
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
//#define int long long
//#define double long double
using i64 = long long;
using ui64 = unsigned long long;
using i128 = __int128;
#define inf (int)0x3f3f3f3f3f3f3f3f
#define INF 0x3f3f3f3f3f3f3f3f
#define yn(x) cout << (x ? "yes" : "no") << endl
#define Yn(x) cout << (x ? "Yes" : "No") << endl
#define YN(x) cout << (x ? "YES" : "NO") << endl
#define mem(x, i) memset(x, i, sizeof(x))
#define cinarr(a, n) for (int _ = 1; _ <= n; _++) cin >> a[_]
#define cinstl(a) for (auto& _ : a) cin >> _
#define coutarr(a, n) for (int _ = 1; _ <= n; _++) cout << a[_] << " \n"[_ == n]
#define coutstl(a) for (const auto& _ : a) cout << _ << ' '; cout << endl
#define all(x) (x).begin(), (x).end()
#define md(x) (((x) % mod + mod) % mod)
#define ls (s << 1)
#define rs (s << 1 | 1)
#define ft first
#define se second
#define pii pair<int, int>
#ifdef DEBUG
    #include "debug.h"
#else
    #define dbg(...) void(0)
#endif

const int N = 5e5 + 5;
//const int M = 1e5 + 5;
const int mod = 998244353;
//const int mod = 1e9 + 7;
//template <typename T> T ksm(T a, i64 b) { T ans = 1; for (; b; a = 1ll * a * a, b >>= 1) if (b & 1) ans = 1ll * ans * a; return ans; }
//template <typename T> T ksm(T a, i64 b, T m = mod) { T ans = 1; for (; b; a = 1ll * a * a % m, b >>= 1) if (b & 1) ans = 1ll * ans * a % m; return ans; }

int a[N];
int n, m, t, k, q;

int fa[N];
int head[N], tail[N], sz[N], to[N], nxt[N], cnt;
i64 d[N];

void add(int u, int v) {
    ++cnt;
    if (!sz[u]) tail[u] = cnt;
    to[cnt] = v;
    nxt[cnt] = head[u];
    head[u] = cnt;
    sz[u]++;
}
void merge(int u, int v) {
    if (!sz[v]) return;
    if (!sz[u]) head[u] = head[v];
    else nxt[tail[u]] = head[v];
    tail[u] = tail[v];
    sz[u] += sz[v];
}

int dep[N], l[N], r[N], tot;
vector<int> dfn;
void dfs(int u) {
    l[u] = ++tot;
    dfn.emplace_back(u);
    for (int i = head[u]; i; i = nxt[i]) {
        int v = to[i];
        dep[v] = dep[u] + 1;
        dfs(v);
    }
    r[u] = tot;
}
template <typename T> struct SegmentTree {
    struct TreeNode { int l, r; T add, st, sum, mx, mn; } tr[N << 2];
    void pushup(int s) {
        tr[s].sum = tr[ls].sum + tr[rs].sum;
        tr[s].mx = max(tr[ls].mx, tr[rs].mx);
        tr[s].mn = min(tr[ls].mn, tr[rs].mn);
    }
    void pushdown(int s) {
        if (tr[s].st != numeric_limits<T>::min()) {
            tr[s].st += tr[s].add;
            tr[ls].add = tr[rs].add = 0;
            tr[ls].st = tr[rs].st = tr[s].st;
            tr[ls].sum = tr[s].st * (tr[ls].r - tr[ls].l + 1);
            tr[rs].sum = tr[s].st * (tr[rs].r - tr[rs].l + 1);
            tr[ls].mx = tr[rs].mx = tr[s].st;
            tr[ls].mn = tr[rs].mn = tr[s].st;
            tr[s].st = numeric_limits<T>::min();
            tr[s].add = 0;
        }
        else if (tr[s].add) {
            tr[ls].add += tr[s].add;
            tr[rs].add += tr[s].add;
            tr[ls].sum += tr[s].add * (tr[ls].r - tr[ls].l + 1);
            tr[rs].sum += tr[s].add * (tr[rs].r - tr[rs].l + 1);
            tr[ls].mx += tr[s].add;
            tr[rs].mx += tr[s].add;
            tr[ls].mn += tr[s].add;
            tr[rs].mn += tr[s].add;
            tr[s].add = 0;
        }
    }
    void build(int l, int r, int s = 1) {
        tr[s].l = l, tr[s].r = r;
        tr[s].add = T(), tr[s].st = numeric_limits<T>::min();
        tr[s].sum = T(), tr[s].mx = numeric_limits<T>::min(), tr[s].mn = numeric_limits<T>::max();
        if (l == r) {
            tr[s].sum = tr[s].mx = tr[s].mn = dep[dfn[l - 1]];
            return;
        }
        int mid = l + r >> 1;
        if (l <= mid) build(l, mid, ls);
        if (mid < r) build(mid + 1, r, rs);
        pushup(s);
    }
    void update(int l, int r, T val, int s = 1) {
        if (l <= tr[s].l && tr[s].r <= r) {
            tr[s].add += val;
            tr[s].sum += val * (tr[s].r - tr[s].l + 1);
            tr[s].mx += val;
            tr[s].mn += val;
            return;
        }
        pushdown(s);
        int mid = tr[s].l + tr[s].r >> 1;
        if (l <= mid) update(l, r, val, ls);
        if (mid < r) update(l, r, val, rs);
        pushup(s);
    }
    void modify(int l, int r, T val, int s = 1) {
        if (l <= tr[s].l && tr[s].r <= r) {
            tr[s].add = T();
            tr[s].st = val;
            tr[s].sum = val * (tr[s].r - tr[s].l + 1);
            tr[s].mx = tr[s].mn = val;
            return;
        }
        pushdown(s);
        int mid = tr[s].l + tr[s].r >> 1;
        if (l <= mid) modify(l, r, val, ls);
        if (mid < r) modify(l, r, val, rs);
        pushup(s);
    }
    T query(int l, int r, int s = 1) {
        if (l <= tr[s].l && tr[s].r <= r) return tr[s].sum;
        int mid = tr[s].l + tr[s].r >> 1;
        T ans = T();
        pushdown(s);
        if (l <= mid) ans += query(l, r, ls);
        if (mid < r) ans += query(l, r, rs);
        return ans;
    }
    T queryMax(int l, int r, int s = 1) {
        if (l <= tr[s].l && tr[s].r <= r) return tr[s].mx;
        int mid = tr[s].l + tr[s].r >> 1;
        T ans = numeric_limits<T>::min();
        pushdown(s);
        if (l <= mid) ans = max(ans, queryMax(l, r, ls));
        if (mid < r) ans = max(ans, queryMax(l, r, rs));
        return ans;
    }
    T queryMin(int l, int r, int s = 1) {
        if (l <= tr[s].l && tr[s].r <= r) return tr[s].mn;
        int mid = tr[s].l + tr[s].r >> 1;
        T ans = numeric_limits<T>::max();
        pushdown(s);
        if (l <= mid) ans = min(ans, queryMin(l, r, ls));
        if (mid < r) ans = min(ans, queryMin(l, r, rs));
        return ans;
    }
};
SegmentTree<int> T;

void work() {
    cin >> n >> m;
    for (int i = 2; i <= n; i++) {
        cin >> fa[i];
        add(fa[i], i);
    }
    cinarr(d, n);
    dfs(1);
    T.build(1, n);

    while (m--) {
        int op, u;
        cin >> op >> u;
        if (op == 1) {
            int tmp = head[u];
            head[u] = tail[u] = sz[u] = 0;
            for (int i = tmp; i; i = nxt[i]) {
                int v = to[i];
                d[u] += d[v];
                merge(u, v);
            }
            cout << sz[u] << ' ' << d[u] << endl;
            if (l[u] + 1 <= r[u]) T.update(l[u] + 1, r[u], -1);
        }
        else cout << T.query(l[u], l[u]) + 1 << endl;
    }
}

signed main() {
#ifdef LOCAL
    freopen("C:\\Users\\admin\\CLionProjects\\Practice\\data.in", "r", stdin);
    freopen("C:\\Users\\admin\\CLionProjects\\Practice\\data.out", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int Case = 1;
    //cin >> Case;
    while (Case--) work();
    return 0;
}
/*
     _____   _   _       _  __    __
    |  _  \ | | | |     | | \ \  / /
    | |_| | | | | |     | |  \ \/ /
    |  ___/ | | | |  _  | |   }  {
    | |     | |_| | | |_| |  / /\ \
    |_|     \_____/ \_____/ /_/  \_\
*/
