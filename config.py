from pathlib import Path
class ProjectPaths:
    def __init__(self):
        self.root = Path(__file__).parent
        self.assets = self.root / "assets"
        self.outputs = self.root / "outputs"
        self.code = self.root / "code"
        self.models = self.root / "models"



    def get_data_file(self, filename):
        """Get path to data file as a string"""
        return str(self.data / filename)
PATHS = ProjectPaths()