from .BaseEnum import BaseEnum
class Endpoint(BaseEnum):
    """
    The endpoint that you want to access to retrieve information from the Hi-Rez Studios' API.
    """
    PALADINS = "http://api.paladins.com/paladinsapi.svc"
    REALM_ROYALE = "http://api.realmroyale.com/realmapi.svc"
    SMITE = "http://api.smitegame.com/smiteapi.svc"
    HIREZ = "https://api.hirezstudios.com"
    STATUS_PAGE = "http://status.hirezstudios.com" #http://stk4xr7r1y0r.statuspage.io

    HAND_OF_THE_GODS = "http://api.handofthegods.com/handofthegodsapi.svc"
    PALADINS_STRIKE = "http://api.paladinsstrike.com/paladinsstrike.svc"
