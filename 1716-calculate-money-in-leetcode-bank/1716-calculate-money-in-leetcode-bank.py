class Solution:
    def totalMoney(self, n: int) -> int:
        money = [1]
        for i in range(1,n):
            if i % 7 == 0:
                money.append(money[i-7] + 1)
            else:
                money.append(money[i-1] + 1)
        return sum(money)

