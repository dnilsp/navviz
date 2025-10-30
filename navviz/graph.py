def build_graph(nav_data):
    import networkx as nx
    G = nx.DiGraph()
    # nav_data: list of (source_file, route_matches, link_matches)
    # Build a mapping from file to its defined routes
    file_to_routes = {}
    for fpath, routes, _ in nav_data:
        for route in routes:
            file_to_routes.setdefault(fpath, set()).add(route)
            G.add_node(route)
    # Add edges: for each file, from its defined routes to its link destinations
    for fpath, routes, links in nav_data:
        for src in routes:
            for dst in links:
                G.add_edge(src, dst)
    return G
