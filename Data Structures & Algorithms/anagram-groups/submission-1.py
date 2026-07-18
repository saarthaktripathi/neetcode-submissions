class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for i in strs:
            count=[0]*26
            offset=ord('a')
            for char in i:
                count[ord(char)-offset]+=1
            key=tuple(count)

            if key not in map:
                map[key]=[]
            map[key].append(i)
        return list(map.values())