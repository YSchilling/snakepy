import json
import os

class Score:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

class Scoreboard:
    def __init__(self, filepath: str):
        self.filepath = filepath

        self._load_scores_from_file(filepath)

    def save(self):
        self._save_scores_to_file(self.filepath)

    def _load_scores_from_file(self, filepath: str):
        file_exists = os.path.isfile(filepath)

        if file_exists:
            with open(filepath) as file:
                self.scores = json.load(file)
        else:
            self.scores = {}
    
    def _save_scores_to_file(self, filepath: str):
        with open(filepath, "wt") as file:
            file.write(json.dumps(self.scores))