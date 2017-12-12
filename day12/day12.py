import re
# this essay on graphs in python helped https://www.python.org/doc/essays/graphs/


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

if __name__ == "__main__":

    graph = dict()

    file_line = open("input.txt", "r").readlines()

    # populate the graph structure
    for line in file_line:
        m = re.search("\d+", line)
        key = int(m.group(0))
        
        graph[key] = [int(destination) for destination in line.split(">")[1].split(",")]


    # for each process, find if there's a path to process 0
    paths_to_0 = []
    for key in graph.keys():
        path_to_0 = find_path(graph, 0, key)
        if path_to_0 is not None: 
            paths_to_0.append( path_to_0 )

    num_paths_to_0 = len(paths_to_0)
    print(f"Number of programs with a path to 0: {num_paths_to_0}")


    # Now find how many groups there are.  Do it by doing the same thing as part 1,
    # but repeating for each process. But skip checking for it if that process is already in
    # a group

    processes_seen = list()
    num_groups = 0

    for key in graph.keys():
        if key in processes_seen:
            continue
        num_groups += 1
        paths_to_key = []
        for other_key in graph.keys():
            path_to_key = find_path(graph, key, other_key)
            if path_to_key is not None:
                paths_to_key.append( path_to_key )
                processes_seen.extend(path_to_key)

    print(f"Number of groups: {num_groups}")
