from collections import defaultdict

travelData = [["B", "A"], ["D", "C"], ["A", "F"], ["Z", "D"], ["C", "B"]]  # s : d


gp = defaultdict()
total = 0
travelled = set()
for source, destination in travelData:
    if source not in travelled:
        total += 1
    if destination not in travelled:
        total += 1
    travelled.add(source)
    travelled.add(destination)

    gp[source] = destination


def dfs(gp, startNode):
    count = 1
    for neighbour in gp.get(startNode, []):
        count = 1 + dfs(gp, neighbour)
    return count


for key in gp.keys():
    totalCount = dfs(gp, key)
    if totalCount == total:
        res = key


last = None


def getLast(node, gp):
    global last
    if node not in gp:
        last = node
    for neighbour in gp.get(node, []):
        getLast(neighbour, gp)


getLast(res, gp)
print(f"starting city = {res}, last city = {last}")
