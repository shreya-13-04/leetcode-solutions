class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        import heapq

        events.sort(key=lambda x:x[0])
        heap=[]
        i=0
        count=0
        day=1

        while i<len(events) or heap:
            while i<len(events) and events[i][0]<=day:
                heapq.heappush(heap, events[i][1])
                i+=1
            
            while heap and heap[0]<day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                count+=1
                day+=1
            else:
                if i<len(events):
                    day=events[i][0]
        return count


        

        