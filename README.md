# Magical Snake War

## 初始規則
1.  左方玩家：Snake A，操作按鍵為 W A S D
    右方玩家：Snake B，操作按鍵為 方向鍵

2.  撞到**邊界**或**任意蛇的身體**：死亡
    撞到**對方頭部**：分數較低者死亡
    撞到**對方頭部**且**雙方分數相等**：雙方都死亡
    當有玩家死亡時，遊戲結束

3.  身體長度為 [分數+2]
    每吃一個莓果可以使自己分數增加一分

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
