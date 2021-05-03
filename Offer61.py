class Solution:
    def isStraight(self, nums) -> bool:
        record, minCard, maxCard = set(), 14, 0
        for card in nums:
            if card == 0: continue
            if card in record:
                return False
            record.add(card)
            minCard = card if card < minCard else minCard
            maxCard = card if card > maxCard else maxCard
        return maxCard - minCard < 5
            
            
