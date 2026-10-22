class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        sortedList_s = sorted(list_s)
        sortedList_t = sorted(list_t)

        if sortedList_s == sortedList_t:
            return True
        elif sortedList_s != sortedList_t:
            return False