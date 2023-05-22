import random

class lottery:

    def __init__(self):

        self.list_vinster =[
            "solstol",
            "stol",
            "bord",
            "gustavs högra boll",
            "smuls radioaktiva hund",
            "arvids 8:e finger",
            "leos tredje arm",
            "eriks knasterstrumpa",
            "tre halva kromosomer",
            "nisses vänstra boll",
            "tre sprutor ebola",
            "sju liter mystiskt skum",
            "en nyligt aktiverad atombomb",
            "Min högra stortå",
            "tre stenar i form av förrädaren från amobnguss",
            "fem kilo badsalt",
            "En femtonårig pojke från sudan",
            "nio badankor fyllda med sprängmedel",
            "4,89 kg av ren amfetamin",
            "michelle obamas största tånagel"
        ]

    def get_vinst(self):
        slumptal = random.randint(0,19)
        return self.list_vinster[slumptal]