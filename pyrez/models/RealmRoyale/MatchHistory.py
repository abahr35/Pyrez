from pyrez.models import APIResponse
from .Match import Match
class MatchHistory(APIResponse):
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.playerId = kwargs.get("id", 0) if kwargs else 0
    	self.playerName = kwargs.get("name", None) if kwargs else None
    	self.matches = [ Match(**_) for _ in (kwargs.get("matches") if kwargs.get("matches", None) else []) ]