class Solution:
    def trap(self, height: List[int]) -> int:
        pref_num=[0] * len(height)
        pref_num[0]=0
        for i in range(1,len(height)):
            pref_num[i]=max(height[i-1],pref_num[i-1])

        suff_num = [0] * len(height)
        suff_num[-1] = 0
        for i in range(len(height) - 2, -1, -1):
            suff_num[i] = max(height[i+1], suff_num[i + 1])

        l,r=0,len(height)-1
        trapped_water=0
        for i,n in enumerate(height):
            water_in_position=min(pref_num[i],suff_num[i])-height[i]
            if water_in_position<=0:
                continue
            trapped_water+=water_in_position

        return trapped_water
                