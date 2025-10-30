# navviz

A Python CLI tool for visualizing navigation endpoints in frontend projects.

## Features
- Detects project language/framework
- Parses navigation/routes (initially for React, extensible to others)
- Generates navigation graphs (Graphviz/NetworkX)
- Outputs diagrams in-terminal (ASCII/Mermaid) or as PDF

## Usage
```
python -m navviz <project_path> [--output pdf|terminal]
```

## Requirements
- Python 3.8+
- See requirements.txt for dependencies

## Roadmap
- [ ] React/JSX navigation parsing
- [ ] Support for other frameworks/languages
- [ ] PDF and terminal output
- [ ] Modular plugin system
