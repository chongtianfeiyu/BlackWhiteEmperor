BlackWhiteEmpiror
=================

黑白皇帝， 一个卡牌游戏。

规则
----
﻿v0.6.7a

卡牌

黑白皇帝(E)x1
黑白骑士(K)x4
黑白游侠(R)x4
黑白刺客(A)x4
士兵(S)x12
商人(M)x12
农民(F)x24

开局：

每人随机发12张牌(必须包含两张皇帝)，剩余牌归入弃牌堆。
拿到皇帝牌的玩家将其亮出，从持有白色皇帝的玩家开始轮流进入玩家各自回合。

胜利条件：

玩家失去所有的牌时被消灭。
持有皇帝的玩家失去所有皇帝即被消灭。

持有两张皇帝的玩家必须消灭其余玩家得胜。
持有一张皇帝的玩家必须亲手消灭另一个持有皇帝的玩家得胜，若另一个持有皇帝的玩家已经被消灭，则该玩家必须消灭其他玩家得胜。
没有皇帝的玩家必须消灭所有的持有皇帝的玩家得胜。

回合开始

换牌阶段：

  外交(必选)：与任意一名玩家同时互换一张牌(除皇帝)，非公开。
  贸易：亮出任意数量的牌(除皇帝)，若其他玩家想要交换，则亮出等量的牌，选一名与之交换，或不交换。

摸牌阶段(单选)：

  农业：取得弃牌堆中的一张农民(若存在)。
  商业：用一张农民交换弃牌堆中的一张商人(若存在)。
  募兵：用一张农民交换弃牌堆中的一张士兵(若存在)。
  拥兵：用一张商人交换弃牌堆中的一张骑士或一张游侠或一张刺客(若存在)。
  练兵：用一张骑士或一张游侠或一张刺客交换弃牌堆中的两张士兵(若存在)。
  召集(皇帝专用)：取得弃牌堆中与皇帝同色的一张骑士或一张游侠或一张刺客(若存在)。

出牌阶段(单选)：

  进攻：对一名玩家列出进攻牌(公开)，攻击列数不得大于对方的所持牌数，相同类型的进攻牌可编入同一列；对方须列出列数与进攻牌列数相等的防御牌，相同类型的防御牌可编入同一列，每一列进攻牌与防御牌对应互为对手牌，按照效果说明进行处理。
        持有一张皇帝的玩家只可使用与所持皇帝同色的牌或无色牌进攻，没有皇帝的玩家只可使用与皇帝反色的牌或无色牌进攻持有一张皇帝的玩家。

    效果说明：同一列进攻牌数大于对手防御牌数，只产生进攻效果，无防御效果。
      捕获：不失去此列牌，获得等量对手牌(对手牌不足则为全部对手牌)。
      消灭：不失去此列牌，等量对手牌进入弃牌堆(对手牌不足则为全部对手牌)。
      收买：失去此列任意数量的牌，获得等量对手牌(对手牌不足则为全部对手牌)。
      聚死：此列牌与等量对手牌皆进入弃牌堆(对手牌不足则为全部对手牌)。
      击退：双方都不失去各自的牌。

    进攻牌：
      皇帝：E.消灭 K.消灭 R.消灭 A.消灭 S.捕获 M.捕获 F.捕获
      骑士：E.消灭 R.捕获 S.消灭 M.捕获 F.捕获
      游侠：E.消灭 A.捕获 S.消灭 M.捕获 F.捕获
      刺客：E.消灭 K.捕获 S.消灭 M.捕获 F.捕获
      士兵：M.捕获 F.消灭
      商人：K.收买 R.收买 A.收买 F.消灭
      农民：M.消灭

    防御牌：
      皇帝：S.消灭  M.消灭 F.消灭
      骑士：K.聚死 R.击退 S.消灭 F.捕获
      游侠：R.聚死 A.击退 S.消灭 F.捕获
      刺客：K.击退 A.聚死 S.消灭 F.捕获
      士兵：S.聚死 M.消灭 F.消灭
      商人：M.击退
      农民：F.聚死

  增援：赠与任意一名玩家任意数量的牌(除皇帝)，公开。

回合结束