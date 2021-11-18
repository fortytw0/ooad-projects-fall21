from src.controllers.abstract_controller import AbstractController
from src.views.blackjack_view import GameView
from src.models.blackjack_model import BlackJackModel
from src.models.user_model import UserModel
from src.lib.blackjack.game import BlackJack
from src.lib.blackjack.dealer import Dealer
from src.lib.blackjack.utils import calculate_result

class BlackJackGame(AbstractController) : 

    def __init__(self):

        '''
        This will typically happen outside the controller : 
        '''

        self.view = GameView()
        self.game_model = BlackJackModel()
        self.user_model = UserModel()
        self.black_jack = BlackJack(1)

        self.highest_score = 0
        self.highest_players = []
        self.player_turn_ctr = 0

    def execute(self):

        self.view.render(method="POST", message="Dealing...\n...\n...\n...")
        self.black_jack.opening_deal()
        
        while self.player_turn_ctr < self.black_jack.num_players-1:
            
            self.view.render(method="POST", 
                            message="Now starting with player : {}".format(self.player_turn_ctr),
                            leading_elipsis=3)
                            
            player_hand = self.black_jack.pit[self.player_turn_ctr]
            
            player_hand = self._player_loop(player_hand)
            self._judge_score(player_hand)

            self.player_turn_ctr += 1
        
        player_hand = self.black_jack.pit[self.player_turn_ctr]
        player_hand = self._player_loop(player_hand, is_dealer=True)
        self._judge_score(player_hand)
        

    def update_state(self):
        print("Update State")

    def transition(self):
        print("Transition")

    def _player_loop(self, player_hand:dict, is_dealer:bool=False)->dict:
        player_turn = player_hand['valid']

        self.view.render(method="POST", 
                        message="These are your starting cards : {}".format(player_hand['cards']),  
                        player_num=self.player_turn_ctr)
        
        while player_turn : 
            
            self.view.render(method="POST", 
                            message="Your score is : {}".format(player_hand['score']), 
                            player_num=self.player_turn_ctr)        

            if is_dealer : 
                self.view.render(method="POST", 
                                message="Do you wish to 1. hit or 2. stay?", 
                                player_num=self.player_turn_ctr)

                selected_action = Dealer().dealer_actions(self.highest_score, player_hand)

            else : 
                selected_action = self.view.render(method="GET", 
                                                message="Do you wish to 1. hit or 2. stay?\n->", 
                                                player_num=self.player_turn_ctr)
                
            player_hand = self.black_jack.player_action(self.player_turn_ctr, selected_action)
            player_turn = player_hand['valid'] & ~player_hand['blackjack']

            self.view.render(method="POST", 
                            message="Your cards are : {}".format(player_hand['cards']),  
                            player_num=self.player_turn_ctr)

        return player_hand

    def _judge_score(self, player_hand:dict)->None : 

        result = calculate_result(player_hand['score'], self.highest_score)

        if result=='bust':
            self.view.render(method="POST", 
                            message="You're bust! Your score is : {}".format(player_hand['score']),  
                            player_num=self.player_turn_ctr)

        elif result=='highscore':

            self.view.render(method="POST", 
                            message="You've matched the highest score! Your score is {}".format(player_hand['score']),  
                            player_num=self.player_turn_ctr)

            self.highest_players.append(self.player_turn_ctr)

        elif result=='new-highscore':

            self.view.render(method="POST", 
                            message="You've got the new highest score! Your score is {}".format(player_hand['score']),  
                            player_num=self.player_turn_ctr)

            self.highest_players = [self.player_turn_ctr]
            self.highest_score = player_hand['score']

        else : 

            if player_hand['score']==21: 
                self.view.render(method="POST", 
                            message="You got the highest possible score! Your score is {}".format(player_hand['score']),  
                            player_num=self.player_turn_ctr)
                
                self.highest_players = [self.player_turn_ctr]
                self.highest_score = player_hand['score']
            
            else: 
                self.view.render(method="POST", 
                            message="Your score is valid, but not the highest! Your score is {}".format(player_hand['score']),  
                            player_num=self.player_turn_ctr)




        
if __name__ == '__main__' : 

    game = BlackJackGame()
    game.execute()


