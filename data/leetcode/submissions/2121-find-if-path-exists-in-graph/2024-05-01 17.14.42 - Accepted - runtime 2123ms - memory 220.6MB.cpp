class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        
        if (!edges.size()) return source == destination;
        vector<vector<int>> graph(n);
        for (vector<int>& edge : edges)
        {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        if (!graph[source].size()) return false;
        queue<int> toBeVisited;
        for (int n : graph[source])
        {
            toBeVisited.push(n);
        }
        int curr;
        vector<int> visited(n, 0);
        while (toBeVisited.size())
        {
            int curr = toBeVisited.front();
            visited[curr] = 1;
            toBeVisited.pop();
            if (curr == destination)
            {
                return true;
            }
            for (int n : graph[curr])
            {
                if (!visited[n])
                toBeVisited.push(n);
            }
        }
        return false;
    }
};