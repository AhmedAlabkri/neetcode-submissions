class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {} # {int : 3, int : 2}

        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
            
        pairs = []
        
        for key, v in my_dict.items():
            pairs.append((key,v))
        
        result = []

        pairs.sort(key=lambda pair: pair[1])

        for i in range(len(pairs) - 1, -1, -1):
            result.append(pairs[i][0])
            if len(result) == k:
                return result



        


        
        