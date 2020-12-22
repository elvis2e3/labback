  #include <string>
  #include <iostream>
  #include <algorithm>
  using namespace std;
  
  const int MAX_N = 100002;
  int sa[MAX_N], rk[MAX_N], lcp[MAX_N], tmp[MAX_N], n, k;

  bool compare_suffix_array(int i, int j) {
     if (rk[i] != rk[j]) return rk[i] < rk[j];
     int ri = i + k <= n ? rk[i + k] : -1;
     int rj = j + k <= n ? rk[j + k] : -1;
     return ri < rj;
  }

  void construct_suffix_array(const string &S, int *sa) {
     n = S.length();
     for (int i = 0; i <= n; i++) {
         sa[i] = i;
         rk[i] = i < n ? S[i] : -1;
     }

     for (k = 1; k <= n; k *= 2) {
         sort(sa, sa + n + 1, compare_suffix_array);

         tmp[sa[0]] = 0;
         for (int i = 1; i <= n; i++) {
             tmp[sa[i]] = tmp[sa[i - 1]] + (compare_suffix_array(sa[i - 1], sa[i]) ? 1 : 0);
         }
         for (int i = 0; i <= n; i++) rk[i] = tmp[i];
     }
 }

  void construct_lcp(const string &S, int *sa, int *lcp) {
     n = S.length();
     for (int i = 0; i <= n; i++) rk[sa[i]] = i;

     int h = 0;
     lcp[0] = 0;
     for (int i = 0; i < n; i++) {
         int j = sa[rk[i] - 1];

         if (h > 0) h--;
         for (; i + h < n && j + h < n; h++) if (S[i + h] != S[j + h]) break;

         lcp[rk[i] - 1] = h;
     }
  }

 string S;
 int lft[MAX_N], rgt[MAX_N], st[MAX_N], top;
 void resolve() {
     construct_suffix_array(S, sa);
     construct_lcp(S, sa, lcp);
     
     lcp[n] = n - sa[n];

     top = 0;
     for (int i = 1; i <= n; i++) {
         while (top && lcp[st[top-1]] >= lcp[i]) top--;
         if (top) lft[i] = st[top - 1] + 1;
         else lft[i] = 1;
         st[top++] = i;
     }
     top = 0;
     for (int i = n; i > 0; i--) {
         while (top && lcp[st[top-1]] >= lcp[i]) top--;
         if (top) rgt[i] = st[top - 1];
         else rgt[i] = n;
         st[top++] = i;
     }
     long long ans = n;
     for (int i = 1; i <= n; i++) ans = max(ans, (long long)lcp[i] * (rgt[i] - lft[i] + 1));
     cout << ans << endl;
 }
 
 int main(void) {
     while (cin >> S) resolve();
     return 0;
 }
