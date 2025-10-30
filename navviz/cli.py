import argparse
from .parser import detect_project_type, parse_navigation
from .graph import build_graph
from .output import output_graph

def main():
    parser = argparse.ArgumentParser(description="Visualize frontend project navigation.")
    parser.add_argument(
        "project_path",
        nargs="?",
        default=".",
        help="Path to the project root (default: current directory)"
    )
    parser.add_argument(
        "-o", "--output",
        choices=["terminal", "pdf", "mermaid"],
        default="terminal",
        help="Output format: terminal (default), pdf, or mermaid"
    )
    args = parser.parse_args()

    project_type = detect_project_type(args.project_path)
    print(f"[DEBUG] Detected project type: {project_type}")
    nav_data = parse_navigation(args.project_path, project_type)
    print(f"[DEBUG] Navigation data: {nav_data}")
    graph = build_graph(nav_data)
    output_graph(graph, args.output)

if __name__ == "__main__":
    main()
