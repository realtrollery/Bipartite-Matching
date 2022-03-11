def dfs(node):
    if visit[node] == 1:
        return 0
    visit[node] = 1

    for c in connect[node]:
        if noteBook[c] == -1 or dfs(noteBook[c]) == 1:
            noteBook[c] = node
            return 1

    return 0
