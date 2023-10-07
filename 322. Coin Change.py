class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        dpList = [0]
        for currAmt in range(1, amount + 1):
            dpList.append(math.inf)
            for coin in coins:
                if coin <= currAmt:
                    if dpList[currAmt - coin] == math.inf:
                        continue
                    else:
                        dpList[-1] = min(dpList[-1], 1 + dpList[currAmt - coin])
        return dpList[-1] if dpList[-1] != math.inf else -1
