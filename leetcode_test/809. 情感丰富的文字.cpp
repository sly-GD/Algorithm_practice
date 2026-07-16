class Solution {
public:
    int expressiveWords(string s, vector<string>& words) {
        int res = 0;
        const string &target = s;
        for (const string &word : words) {
            // 单词更长直接跳过
            if (word.size() > target.size()) continue;
            int i = 0, j = 0;
            bool valid = true;
            while (i < target.size() && j < word.size()) {
                // 当前字符不匹配，直接无效
                if (target[i] != word[j]) {
                    valid = false;
                    break;
                }
                // 统计target当前段长度
                int ti = i;
                while (ti < target.size() && target[ti] == target[i]) ti++;
                int cnt_s = ti - i;

                // 统计word当前段长度
                int wj = j;
                while (wj < word.size() && word[wj] == word[j]) wj++;
                int cnt_w = wj - j;

                // 拉伸规则校验
                if (cnt_w > cnt_s) {
                    valid = false;
                    break;
                }
                // 原段不足3个，必须长度相等
                if (cnt_s < 3 && cnt_s != cnt_w) {
                    valid = false;
                    break;
                }

                i = ti;
                j = wj;
            }
            // 必须两段都完全遍历完，且中间全程合法
            if (valid && i == target.size() && j == word.size()) {
                res++;
            }
        }
        return res;
    }
};
