import pandas as pd
import numpy as np


class InvalidScoreError(ValueError):
    """Raised when a student score fails validation rules."""
    def __init__(self, score, message="Score must be between 0 and 100"):
        self.score = score
        self.message = f"{message}: {score}"
        super().__init__(self.message)


raw_rows = [
    {"name": " Amara ", "scores": "92,85,78"},
    {"name": "Leo", "scores": "88,91,73"},
    {"name": "Priya", "scores": "65,72,150"},         
    {"name": "Sam", "scores": "70,not_a_number,60"},  
    {"name": "Amara", "scores": "95,90,88"},          
    {"name": "Jade", "scores": "81,77,84,90"},
]

df = pd.DataFrame(raw_rows)
print(df)

class student (Exception):
    def __init__  (self name, scores)
 self.Name = Name
 self.Scores = scores

def average

def __str__(self):
        return f"{self.name} ({self.scores}

