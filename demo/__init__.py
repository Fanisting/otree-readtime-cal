from otree.api import *


doc = """
Calculate the time of 
"""


class C(BaseConstants):
    NAME_IN_URL = 'demo'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time = models.FloatField()


# PAGES
class show(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            pdf_path='demo.pdf'
        )
    @staticmethod
    def live_method(player, data):
        player.time = data

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [show, Results]
