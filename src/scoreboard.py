import json
import os

class Scoreboard:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.scores: list[dict] = []

        self._load_scores_from_file(filepath)

    def save(self):
        self._save_scores_to_file(self.filepath)

    def add_score(self, new_score) -> None:
        self.scores.append(new_score)
        self.scores.sort(key=lambda score: score["score"], reverse=True)

    def _load_scores_from_file(self, filepath: str) -> None:
        file_exists = os.path.isfile(filepath)

        if file_exists:
            with open(filepath) as file:
                self.scores = json.load(file)
        else:
            self.scores = []
    
    def _save_scores_to_file(self, filepath: str) -> None:
        with open(filepath, "wt") as file:
            file.write(json.dumps(self.scores))