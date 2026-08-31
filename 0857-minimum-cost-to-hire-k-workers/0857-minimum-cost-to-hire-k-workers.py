class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        import heapq
        workers=[]

        for i in range(len(quality)):
            ratio=wage[i]/quality[i]
            workers.append((ratio, quality[i]))

        workers.sort()

        heap=[]
        quality_sum=0
        answer=float('inf')

        for ratio, q in workers:
            heapq.heappush(heap, -q)
            quality_sum+=q

            if len(heap)>k:
                removed= -heapq.heappop(heap)
                quality_sum-=removed
            if len(heap)==k:
                cost = ratio*quality_sum
                answer=min(answer, cost)
        return answer

        