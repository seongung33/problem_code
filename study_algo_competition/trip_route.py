# def solution(tickets):
    
#     def dfs(cnt, N, tickets):
#             nonlocal answer, valid, visited
#             if valid:
#                  return
#             if cnt == N+1:
#                 # print(answer)
#                 valid = True
#                 return
#             ans = []
#             for i in range(N):
#                 if visited[i]:
#                     continue
#                 if answer[-1] == tickets[i][0]:
#                     ans.append((tickets[i][1], i))
#             ans.sort()
#             next_air, idx = ans[0]
#             visited[idx] = True
#             answer.append(next_air)
#             dfs(cnt+1, N, tickets)
#             if valid:
#                  return
#             answer.pop()
#             visited[idx] = False

#     N = len(tickets)
#     tickets.sort(key= lambda x:x[1])
#     print(tickets)
#     answer = ["ICN"]
#     visited = [False]*N
#     valid = False
#     dfs(1, N, tickets)
#     print(answer)
#     return answer

def solution(tickets):
    
    def dfs(cnt, N, tickets):
            nonlocal answer, valid, visited
            if valid:
                 return
            if cnt == N+1:
                # print(answer)
                valid = True
                return
            for i in range(N):
                if visited[i]:
                    continue
                if answer[-1] == tickets[i][0]:
                    visited[i] = True
                    answer.append(tickets[i][1])
                    dfs(cnt+1, N, tickets)
                    visited[i] = False
                    if valid:
                        return
                    answer.pop()

    N = len(tickets)
    tickets.sort(key= lambda x:x[1])
    print(tickets)
    answer = ["ICN"]
    visited = [False]*N
    valid = False
    dfs(1, N, tickets)
    print(answer)
    return answer
