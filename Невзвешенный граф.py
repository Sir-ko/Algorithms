#имя == искомое? нет? добавляем соседей "имя", повторяем
def BFS(graph, name):
    queue = [graph["I"]]
    checked = []
    while queue:
        if queue[0] != name and name not in checked and True: #Вместо True может быть любое условие поиска узла
            queue += graph[name]
            checked.append(name)
        else:
            print("found him!")
            return 1
    return -1

#example
graph = dict()
graph['I'] = {"Alice", "Bob", "Clare"}
graph['Bob'] = {"Anuj", "Peggy"}
graph["Alica"] = {'Peggy'}
graph["Clare"] = {'Tom', 'Johny'}
graph['Tom'] = []
graph["Peggy"] = []
graph["Johny"] = []
#example
add_nodes(graph, 'I')
print(BFS(graph, "Johny"))