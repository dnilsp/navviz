def detect_project_type(project_path):
    import os
    files = set(os.listdir(project_path))
    if "package.json" in files:
        # Scan all subdirectories for .jsx/.tsx files
        for root, _, filenames in os.walk(project_path):
            for f in filenames:
                if f.endswith(".jsx") or f.endswith(".tsx"):
                    return "react"
        return "node"
    if "requirements.txt" in files:
        return "python"
    if "angular.json" in files:
        return "angular"
    if "pubspec.yaml" in files:
        return "flutter"
    return "unknown"

def parse_navigation(project_path, project_type):
    import os
    import re
    print(f"[DEBUG] Entered parse_navigation for project_type: {project_type}")
    nav_data = []  # List of (source_file, route_matches, link_matches)
    if project_type == "react":
        print(f"[DEBUG] Scanning for routes in: {project_path}")
        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if not d.startswith('node_modules') and not d.startswith('.')]
            if 'node_modules' in root or '/.' in root or '\\.' in root:
                continue
            for fname in files:
                if fname.endswith((".js", ".jsx", ".ts", ".tsx")):
                    fpath = os.path.join(root, fname)
                    print(f"[DEBUG] Reading file: {fpath}")
                    try:
                        with open(fpath, encoding="utf-8") as f:
                            content = f.read()
                        content_flat = re.sub(r'\s+', ' ', content)
                        route_matches = [m.strip() for m in re.findall(r'<Route[^>]*?path\s*=\s*["\']([^"\']+)["\'][^>]*/?>', content_flat) if m.strip().startswith("/")]
                        link_matches = [m.strip() for m in re.findall(r'<Link[^>]*?to\s*=\s*["\']([^"\']+)["\'][^>]*/?>', content_flat) if m.strip().startswith("/")]
                        obj_matches = [m.strip() for m in re.findall(r'path\s*:\s*["\']([^"\']+)["\']', content_flat) if m.strip().startswith("/")]
                        # Merge object style matches into route_matches
                        route_matches += obj_matches
                        nav_data.append((fpath, route_matches, link_matches))
                        print(f"[DEBUG] Route matches: {route_matches}")
                        print(f"[DEBUG] Link matches: {link_matches}")
                    except Exception as e:
                        print(f"[DEBUG] Error reading {fpath}: {e}")
                        continue
    # TODO: Add support for other frameworks
    return nav_data
