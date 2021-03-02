# Magical Snake War ver 1.1.0

## 初始規則

1.  操作方式
    * 左方玩家：Snake A，按鍵為 W A S D
    * 右方玩家：Snake B，按鍵為 方向鍵

2.  遊戲結束
    * 撞到**邊界**或**任意蛇的身體**：死亡
    * 撞到**對方頭部**：分數較低者死亡
    * 撞到**對方頭部**且**雙方分數相等**：雙方都死亡
    * 當有玩家死亡時，遊戲結束

3.  莓果機制
    * 身體長度為 [分數+2]
    * 吃莓果可以使自己分數增加

4.  開始遊戲
    * 從終端機下載 pygame (如果已經下載過就不用)
        ```console
        pip install pygame
        ```
    * 閱讀 READ.MD 內的規則和玩法
    * 使用任何 Python 的 IDE 執行 main.py
    * 有任何意見或發現任何 bug 都可以跟我說😃😃

---

## 版本

### ver 1.0.0 beta

* 莓果規則更新
    * 場上永遠存在三顆莓果
    * 新生成莓果的座標不會與蛇的身體或其它莓果重疊
    * 莓果有三個階段：紅色(1分)、藍色(3分)、閃光彩色(5分)
    * 三個階段生成的機率分別為：57%、29%、14%
    
* 莓果的 remote 值
    * 每個莓果都具有獨立的 remote 值，剛生成時為 0 (包括初始莓果)
    * 當一個莓果被任何蛇吃掉時，其它莓果的 remote 值會增加 1
    * 當 remote 值達到 6 之後，該莓果會進化到下一個階段且 remote 值歸 0
    * 換句話說，也就是當某個莓果都沒人要吃的時候，其吸引力就會增加
    
* Bugs Found：
    * 當蛇靠近邊緣時，有可能會導致自己因撞到自己身體而死亡
    為了 debug，每次遊戲結束前會輸出死亡原因及相關資料以供參考

* 計畫：
    * 增加不同顏色的蛇，且具備不同的技能
    * 遊戲速度可能隨時間加快

* 更新：
    * ver 1.0.1：修復了撞到頭部的判定結果
    * ver 1.0.2：修復了莓果生成在蛇身上卻沒重置的錯誤、刪除重複函式庫

### ver 1.1.0 beta

* 遊戲規則更新
    * 因任何原因導致，雙方同時死亡時，分數較低者遊戲失敗

* 遊戲速度
    * 遊戲速度將隨著莓果收集的數量增加
    (收集的莓果總數每增加 10 顆，速度等級增加 1)

* Bugs Found：
    * 當快速進行按鍵時，蛇有可能會導致自己因撞到自己身體而死亡
    為了 debug，每次遊戲結束前會輸出死亡原因及相關資料以供參考
    * 有時莓果會顯示但無法採集，推測可能座標有誤
    為了 debug，當按下 空白鍵 時，輸出兩隻蛇的頭部座標及所有莓果座標

* 計畫：
    * 增加不同顏色的蛇，且具備不同的技能

### ver 1.1.1 beta

* Bugs Found：
    * 修復畫面閃爍問題
