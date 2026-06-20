class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        M=len(points)
        if M==1: return 1
        lines=defaultdict(set)
        for i in range(M):
            for j in range(i+1,M):
                u,v=points[i],points[j]
                u_x,u_y,v_x,v_y=u[0],u[1],v[0],v[1]
                if u_x==v_x:
                    lines[u_x].add(u_y)
                    lines[u_x].add(v_y)
                else:
                    a=(v_y-u_y)/(v_x-u_x)
                    b=v_y-a*v_x
                    lines[(a,b)].add((u_x,u_y))
                    lines[(a,b)].add((v_x, v_y))
        return len(lines[max(lines, key=lambda line: len(lines[line]))])
        