import json
import os
import pygame
from game_settings import GameSettings

class Scoreboard:
    def __init__(self, filepath: str, game) -> None:
        self.game = game
        self.filepath = filepath
        self.scores: list[dict] = []
        self.new_name = []
        self.is_new_name_finished = False

        self._load_scores_from_file(filepath)

    def save(self):
        self._save_scores_to_file(self.filepath)

    def add_score(self, new_score) -> None:
        self.scores.append(new_score)
        self.scores.sort(key=lambda score: score["score"], reverse=True)

    def draw(self) -> None:
        for pos, score in enumerate(self.scores):
            if pos >= 10: break
            text = f"{pos+1}: {score['score']} {score['name']}"
            self.game._draw_center_text(text, 64+48*pos)

    def draw_set_name_screen(self):
        text = "Your name: " + "".join(self.new_name)
        self.game._draw_center_text(text, GameSettings.WINDOW_WIDTH_AND_HIGHT / 2)

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