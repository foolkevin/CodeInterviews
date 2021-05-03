class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        length1, length2 = len(first), len(second)
        if abs(length1 - length2) > 1:
            return False
        elif length1 == length2:
            return self.oneEditReplace(first, second)
        elif length1 - length2 == 1:
            return self.oneEditInsert(first, second)
        else:
            return self.oneEditInsert(second, first)
        
    def oneEditReplace(self, first: str, second: str) -> bool:
        diff = False
        for char1, char2 in zip(first, second):
            if char1 != char2:
                if diff:
                    return False
                diff = True
        return True

    def oneEditInsert(self, first: str, second: str) -> bool:
        index1, index2 = 0, 0
        while index1 < len(first) and index2 < len(second):
            if first[index1] != second[index2]:
                if index1 != index2:
                    return False
                index1 += 1
            else:
                index1 += 1
                index2 += 1
        return True