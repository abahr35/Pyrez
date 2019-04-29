from .APIResponse import APIResponse
from pyrez.enumerations import Champions
class ChampionCard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activeFlagActivationSchedule = str(kwargs.get("active_flag_activation_schedule", None)).lower() == 'y'
        self.activeFlagLti = str(kwargs.get("active_flag_lti", None)).lower() == 'y'
        self.cardDescription = kwargs.get("card_description", None) if kwargs is not None else None
        self.cardId1 = kwargs.get("card_id1", 0) if kwargs is not None else 0
        self.cardId2 = kwargs.get("card_id2", 0) if kwargs is not None else 0
        self.cardName = kwargs.get("card_name", None) if kwargs is not None else None
        self.cardNameEnglish = kwargs.get("card_name_english", None) if kwargs is not None else None
        self.godCardURL =  kwargs.get("championCard_URL", None) if kwargs is not None else None
        self.godIconURL = kwargs.get("championIcon_URL", None) if kwargs is not None else None
        try:
            self.godId = Champions(kwargs.get("champion_id"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("champion_id", 0) if kwargs is not None else 0
            self.godName = kwargs.get("champion_name", None) if kwargs is not None else None
        self.exclusive = str(kwargs.get("exclusive", None)).lower() == 'y'
        self.rank = kwargs.get("rank", 0) if kwargs is not None else 0
        self.rarity = kwargs.get("rarity", None) if kwargs is not None else None
        self.rechargeSeconds = kwargs.get("recharge_seconds", 0) if kwargs is not None else 0
    def getIconURL(self):
        return "https://web2.hirez.com/paladins/champion-icons/{0}.jpg".format(self.godName.lower().replace(' ', '-'))
    def getCardURL(self):
        return "https://web2.hirez.com/paladins/champion-cards/{0}.jpg".format(self.cardNameEnglish.lower().replace(' ', '-'))