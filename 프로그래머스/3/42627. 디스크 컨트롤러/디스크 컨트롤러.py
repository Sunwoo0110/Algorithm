import heapq

def solution(jobs):
    answer = 0
    
    ## (요청시각, 소요시간, 작업번호)
    jobs = [(s, l, idx) for idx, (s, l) in enumerate(jobs)]
    jobs.sort()
    
    heap = [] ## (소요시간, 요청시각, 작업번호)
    cnt = 0 ## 현재까지 처리한 작업
    jobs_len = len(jobs)
    job_idx = 0
    cur_time = 0
    total_time = 0
    
    while cnt < jobs_len:
        ## 현재 시간에 요청된 작업
        while job_idx < jobs_len and jobs[job_idx][0] <= cur_time:
            s, l, idx = jobs[job_idx]
            heapq.heappush(heap, (l, s, idx))
            job_idx += 1
            
        
        if heap:
            ## 작업 수행
            l, s, idx = heapq.heappop(heap)
            cur_time += l
            total_time += cur_time-s
            cnt += 1
            
        else:
            cur_time = jobs[job_idx][0]
        
    answer = total_time // jobs_len   
        
    return answer