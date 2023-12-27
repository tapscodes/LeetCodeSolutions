class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # sorts the array, lowest to highest
        citations.sort()
        total_papers = 0
        all_papers = True
        # loops through array from 1 paper -> solution until h-index isn't satisfied
        for i in range(len(citations)-1, -1, -1):
            total_papers += 1
            if(citations[len(citations) - total_papers] < total_papers):
                all_papers = False
                break
        # if all papers viable, special case
        if(all_papers):
            return total_papers
        return total_papers - 1