# Simple-fuzzy-searcher 簡易模糊搜尋

A simple fuzzy search tool. I use the BK-tree datastructure and Levenshtein distance to implement. For the Levenshtein distance part, since it's using dynamic programming to accomplish, which can be a little time-consuming, I use a dll file wrote by `Go` to boost the speed.

You can adjust the `dictionary.txt` file to the dataset you want. Note that this data structure(bk-tree) can not store that many datas, because it will take too long to insert. Data size under 10k or 5k is probably acceptable (idk, never tested).

一個簡單的模糊搜尋工具，用到 bk-tree 跟萊文斯坦距離來實作。由於萊文斯坦距離是利用動態規劃(DP)的方式實作的，用`Python`跑可能會有點慢，的部分我是用`Go`語言實作並輸出成 dll 檔，來加速運算。

可以調整 `dictionary.txt` 檔案來變成你想要的字典。注意這個 bk-tree 沒辦法存太多資料，我嘗試存過 9 萬筆資料，總共花了三分鐘讀取，最後找了小一點的資料量 3000 多筆，算是可以接受的量，我估計到 1 萬應該都還可以，就是 tolerance 盡量不要太大就好。

## Example

```py
from FuzzySearcher import FuzzySearcher
# create object
# you can set the tolerace distance and wheather it's case sensitive or not
fuzzy_searcher = FuzzySearcher(tolerance=4, is_case_sensitive=True)

# test word
# which should be "comment"
word = 'coment'
print(fuzzy_searcher.get_best_match(word)) # output: comment

# this will return a list of possible matches
print(fuzzy_searcher.get_possible_matches(word)) # output: [..., 'comment', ...]
```