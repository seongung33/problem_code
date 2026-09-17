from heapq import heappush, heappop

def solution(jobs):
    jobs.sort()
    n = len(jobs)
    t = 0
    total = 0
    pq = []
    idx = 0
    while pq or idx < n:
        while idx < n and jobs[idx][0] <= t:
            start, duration = jobs[idx]
            heappush(pq, (duration, start))
            idx += 1
            print(idx)
            
        
    
        if pq:
            print(pq)
            duration, start = heappop(pq)
            
            t += duration
            
            total += t - start
        else:
            t = jobs[idx][0]
            
    return total // n

solution([[0, 3], [1, 9], [3, 5]])