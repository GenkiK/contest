from sys import stdin

input = stdin.readline

n = int(input().rstrip())
jobs = [list(map(int, input().rstrip().split())) for _ in range(n)]

sorted_jobs = sorted(jobs, key=lambda x: x[1])
cnt = 0
past_job = sorted_jobs[0]
for job in sorted_jobs[1:]:
    if job[0] > past_job[1]:
        cnt += 1
        past_job = job
print(cnt)
