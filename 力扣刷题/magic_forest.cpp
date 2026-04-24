#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
#define lc p<<1
#define rc p<<1|1

const int N = 1e6 + 5;

int w[N];

struct node{
    int max_val;
    ll sum;
}tr[4*N];


int divisor_count[N];

void precompute() {
    for (int i = 1; i < N; ++i) {
        for (int j = i; j < N; j += i) {
            divisor_count[j]++;
        }
    }
}

// ll countFactors(ll n){
//     if(n==1) return 1;

//     ll res=1;
//     int exponent=0;

//     // 2 的因子个数
//     while(n%2==0){
//         exponent++;
//         n/=2;
//     }
//     if (exponent > 0) {
//         res *= (exponent + 1);
//         exponent = 0; // 重置指数
//     }

//     // 3 的因子个数
//     for(int i=3;i*i<=n;i+=2){
//         while(n%i==0){
//             exponent++;
//             n/=i;
//         }
//         if(exponent>0){
//             res*=(exponent+1);
//             exponent=0;
//         }
//     }

//     // 如果 n 是一个大于 2 的素数
//     if(n>1) res*=2;

//     return res;
// }
void push_up(int p){
    tr[p].sum=tr[lc].sum+tr[rc].sum;
    tr[p].max_val=max(tr[lc].max_val,tr[rc].max_val);
}


void Build(int p,int l, int r){
    //tr[p]={l,r,0,w[l]};
    if(l==r) {
        tr[p].sum=w[l];
        tr[p].max_val=w[l];
        return;
    }
    int mid = (l+r)>>1;
    Build(lc,l,mid);
    Build(rc,mid+1,r);
    push_up(p);
}

/**
 * 单点修改
 * 更新线段树节点值的函数
 * @param p 当前节点的索引
 * @param x 需要更新的位置
 */
void update(int p,int start,int end,int l,int r){
    // 关键剪枝：如果当前区间最大值 <= 2，由于 d(1)=1, d(2)=2，值不会再变，直接跳过
    if(tr[p].max_val<=2) return;
    //如果是叶子节点，直接更新
    if(start==end){
        // 对当前节点的sum值进行因子数量计算
        tr[p].sum=divisor_count[tr[p].sum];
        tr[p].max_val=tr[p].sum;
        return;
    }

    // 计算当前区间的中间位置
    int mid = (start + end )>>1;
    // 如果更新位置在左子树，递归更新左子树
    if(l<=mid) update(lc,start,mid,l,r);
    // 否则递归更新右子树
    if(r>mid) update(rc,mid+1,end,l,r);
    // 更新当前节点的sum值，为左右子树sum值之和
    push_up(p);
}

ll query(int p,int start,int end,int l,int r){
    if(r<start || l>end) return 0;
    if(l<=start && end<=r) return tr[p].sum;

    int mid = (start + end )>>1;
    return query(lc,start,mid,l,r)+query(rc,mid+1,end,l,r);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    precompute();
    int n,m;
    cin>>n>>m;
    for(int i=1;i<=n;i++) cin>>w[i];
    
    Build(1,1,n);

    while(m--){
        int op,l,r;
        cin>>op>>l>>r;
        if(op==1) update(1,1,n,l,r);
        else cout<<query(1,1,n,l,r)<<endl;
    }
    return 0;
}


/*
**极致性能优化时间0.73s
*/
// #include <cstdio>
// #include <algorithm>

// using namespace std;

// // --- 极致 Fast I/O ---
// char buf[1 << 21], *p1 = buf, *p2 = buf;
// #define get_char() (p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 1 << 21, stdin), p1 == p2) ? EOF : *p1++)

// inline int read() {
//     int x = 0; char c = get_char();
//     while (c < '0' || c > '9') c = get_char();
//     while (c >= '0' && c <= '9') x = x * 10 + c - '0', c = get_char();
//     return x;
// }

// char obuf[1 << 21], *p3 = obuf;
// inline void putchar_fast(char c) {
//     if (p3 - obuf == (1 << 21)) fwrite(obuf, 1, 1 << 21, stdout), p3 = obuf;
//     *p3++ = c;
// }

// void write(long long x) {
//     if (x > 9) write(x / 10);
//     putchar_fast(x % 10 + '0');
// }

// // --- 常量定义 ---
// const int MAXV = 1000005; // 魔法值上限 1e6
// const int MAXN = 1000005;  // 果实数量上限 1e5 (请根据具体题目要求微调)

// int divisor_count[MAXV];
// int min_prime_cnt[MAXV], primes[MAXV], pcnt;
// bool not_prime[MAXV];

// // --- O(V) 线性筛 ---
// void precompute() {
//     divisor_count[1] = 1;
//     for (int i = 2; i < MAXV; ++i) {
//         if (!not_prime[i]) {
//             primes[pcnt++] = i;
//             divisor_count[i] = 2;
//             min_prime_cnt[i] = 1;
//         }
//         for (int j = 0; j < pcnt && i * primes[j] < MAXV; ++j) {
//             not_prime[i * primes[j]] = true;
//             if (i % primes[j] == 0) {
//                 min_prime_cnt[i * primes[j]] = min_prime_cnt[i] + 1;
//                 divisor_count[i * primes[j]] = divisor_count[i] / (min_prime_cnt[i] + 1) * (min_prime_cnt[i * primes[j]] + 1);
//                 break;
//             } else {
//                 min_prime_cnt[i * primes[j]] = 1;
//                 divisor_count[i * primes[j]] = divisor_count[i] * 2;
//             }
//         }
//     }
// }

// // --- 线段树部分 ---
// struct node {
//     int max_val;
//     long long sum;
// } tr[MAXN << 2];

// int w[MAXN];

// #define lc (p << 1)
// #define rc (p << 1 | 1)

// inline void push_up(int p) {
//     tr[p].sum = tr[lc].sum + tr[rc].sum;
//     tr[p].max_val = max(tr[lc].max_val, tr[rc].max_val);
// }

// void build(int p, int l, int r) {
//     if (l == r) {
//         tr[p].sum = tr[p].max_val = w[l];
//         return;
//     }
//     int mid = (l + r) >> 1;
//     build(lc, l, mid);
//     build(rc, mid + 1, r);
//     push_up(p);
// }

// void update(int p, int start, int end, int l, int r) {
//     // 关键剪枝
//     if (tr[p].max_val <= 2) return;
//     if (start == end) {
//         tr[p].sum = divisor_count[tr[p].sum];
//         tr[p].max_val = (int)tr[p].sum;
//         return;
//     }
//     int mid = (start + end) >> 1;
//     if (l <= mid) update(lc, start, mid, l, r);
//     if (r > mid) update(rc, mid + 1, end, l, r);
//     push_up(p);
// }

// long long query(int p, int start, int end, int l, int r) {
//     if (l <= start && end <= r) return tr[p].sum;
//     int mid = (start + end) >> 1;
//     long long res = 0;
//     if (l <= mid) res += query(lc, start, mid, l, r);
//     if (r > mid) res += query(rc, mid + 1, end, l, r);
//     return res;
// }

// int main() {
//     precompute();
    
//     int n = read();
//     int m = read();
//     for (int i = 1; i <= n; i++) w[i] = read();
    
//     build(1, 1, n);

//     while (m--) {
//         int op = read();
//         int l = read();
//         int r = read();
//         if (op == 1) {
//             update(1, 1, n, l, r);
//         } else {
//             write(query(1, 1, n, l, r));
//             putchar_fast('\n');
//         }
//     }

//     fwrite(obuf, 1, p3 - obuf, stdout); // 最后一次刷新输出缓冲
//     return 0;
// }