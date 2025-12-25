import os

# Define the structure based on your diagram
structure = {
    "sentinel": [
        ".github/workflows/ci.yml",
        "agents/__init__.py",
        "agents/spec_ingestion.py",
        "agents/intent_extraction.py",
        "agents/behavior_monitor.py",
        "agents/drift_detection.py",
        "agents/action_orchestrator.py",
        "config/__init__.py",
        "config/settings.py",
        "config/prompts.py",
        "data/contracts/",
        "data/logs/",
        "data/embeddings/",
        "dashboard/__init__.py",
        "dashboard/app.py",
        "dashboard/components/__init__.py",
        "dashboard/static/",
        "docs/architecture.md",
        "docs/demo_script.md",
        "docs/api_reference.md",
        "pipeline/__init__.py",
        "pipeline/pathway_connector.py",
        "pipeline/orchestrator.py",
        "tests/__init__.py",
        "tests/test_agents.py",
        "tests/test_pipeline.py",
        "tests/test_integration.py",
        ".env.example",
        ".gitignore",
        "LICENSE",
        "README.md",
        "requirements.txt",
        "setup.py",
        "docker-compose.yml"
    ]
}

def create_structure(base_path, tree):
    for folder, items in tree.items():
        for item in items:
            path = os.path.join(base_path, folder, item)
            if item.endswith('/'):
                os.makedirs(path, exist_ok=True)
            else:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, 'w') as f:
                    pass  # Create empty file

if __name__ == "__main__":
    create_structure(".", structure)
    print("Project structure created successfully!")
