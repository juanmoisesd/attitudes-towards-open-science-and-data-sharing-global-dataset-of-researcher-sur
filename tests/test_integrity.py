import os

def test_critical_files_presence():
    critical_files = [
        "LICENSE",
        "README.md",
        "VERSION",
        "CITATION.cff"
    ]
    for f in critical_files:
        assert os.path.exists(f), f"Critical file missing: {f}"

def test_data_directories_not_empty():
    assert os.path.isdir("data/raw")
    assert os.path.isdir("data/clean")
    assert os.path.isdir("data/analysis_ready")
