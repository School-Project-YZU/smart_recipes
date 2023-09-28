# 聰明食譜Line Chatbot
Use selenium to crawl recipe information and make a Line chatbot through fine-tuning.

## 第一次實驗
- 總資料筆數：415
  - 蔬食：50
  - 牛肉：50
  - 豬肉：50
  - 海鮮：50
  - 雞肉：65
  - 甜點：50
  - 羊肉：50
  - 湯點：50

### 實驗結果探討
1. 範圍太廣泛，而蒐集的資料以及種類太少
2. prompt內的keywords未進行規範 
3. 只有1~3個keyword
   - completion內的格式不夠嚴謹，以致有出現錯誤與overlapping的狀況
   - chatbot的輸入方式使系統認為是接續文章而進行生成
### 改進方向
1. 將範圍縮小，縮成一種食材為主的料理
2. 減少種類並增加每個種類的資料量
3. 設定prompt的keywords的規範
4. 將completion內敘述更加有規則

## 第二次實驗
- 總資料筆數：2015
  - 牛肉：505
  - 豬肉：503
  - 雞肉：503
  - 魚肉：504

### 實驗結果探討
1. 部分翻譯錯誤，如:單一字(薑)會被翻成(姜)，但多數字組成的字詞卻翻譯正確(薑片)。
2. 食材的名稱部分有些會生出沒有使用到的食材。

## 完整PPT
- https://www.canva.com/design/DAFR0sidcbc/JX_rPWYLxDgnxoxtsE2iuA/edit?utm_content=DAFR0sidcbc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
