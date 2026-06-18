from pydantic import BaseModel, Field
from typing import Literal


class PredictionRequest(BaseModel):
    # Le texte Ã  analyser : obligatoire, entre 1 et 5000 caractÃ¨res
    text: str = Field(..., min_length=1, max_length=5000)


class PredictionResponse(BaseModel):
    # Le label retournÃ© est contraint Ã  3 valeurs possibles
    label: Literal["POSITIVE", "NEGATIVE", "NEUTRAL"]
    score: float  # Score de confiance entre 0.0 et 1.0
    text: str     # Texte original retournÃ© pour traÃ§abilitÃ©
