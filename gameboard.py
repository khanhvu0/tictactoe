class BoardClass:
    """A class to store and handle information of the user's tic tac toe board

    Attributes:
        user_name (str): The name of the user
        opponent_name (str): The name of the opponent
        lastmove (str): The name of the player who made the lastest move
        wins (int): The number of wins the user have
        losses (int): The number of losses the user have
        ties (int): The number of ties the user have
        games_played (int): The number of games have been played
        board (lst): The user's game board
    """
    
    def __init__(self, user_name: str = "", opponent_name: str = "", lastmove: str = "", wins: int = 0, ties: int = 0, losses: int = 0, games_played: int = 0) -> None:
        """Make a BoardClass with the attributes above.

        Args:
            user_name (str): The name of the user
            opponent_name (str): The name of the opponent
            lastmove (str): The name of the player who made the lastest move
            wins (int): The number of wins the user have
            losses (int): The number of losses the user have
            ties (int): The number of ties the user have
            games_played (int): The number of games have been played
            board (lst): The user's game board
        """
        
        self.user_name = user_name
        self.opponent_name = opponent_name
        self.lastmove = lastmove
        self.wins = wins
        self.ties = ties
        self.losses = losses
        self.games_played = games_played
        self.board = []
    
    def makeBoard(self) -> None:
        """Add empty positions to user's board."""
        for i in range(9):
            self.board.append('-')
            
    def updateGamesPlayed(self) -> None:
        """Keeps track how many games have started"""
        self.games_played += 1    
        
    def updateGameBoard(self, UI) -> None:
        """Update user's board attribute.
        
        Args:
            UI: the tkinter UI object
        """
        self.board = UI.board
    
    def resetGameBoard(self, UI) -> None:
        """Clear all the moves from the user's board"""
        i = 0
        for x in range(9):
            self.board[i] = '-'
            i += 1
        UI.board = self.board
        
    def isWinner(self) -> None | bool:
        """Check if the lastest move resulted in a win or lose and update the 
        wins and losses count.
        
        Returns:
            True if the user wins
            False if the user loses
            None otherwise
        """
        
        win = False
        if self.board[0] == self.board[1] == self.board[2]:
            if self.board[0] == 'x' or self.board[0] == 'o':
                win = True
        if self.board[3] == self.board[4] == self.board[5]:
            if self.board[3] == 'x' or self.board[3] == 'o':
                win = True
        if self.board[6] == self.board[7] == self.board[8]:
            if self.board[6] == 'x' or self.board[6] == 'o':
                win = True
        if self.board[0] == self.board[3] == self.board[6]:
            if self.board[0] == 'x' or self.board[0] == 'o':
                win = True
        if self.board[1] == self.board[4] == self.board[7]:
            if self.board[1] == 'x' or self.board[1] == 'o':
                win = True
        if self.board[2] == self.board[5] == self.board[8]:
            if self.board[2] == 'x' or self.board[2] == 'o':
                win = True
        if self.board[0] == self.board[4] == self.board[8]:
            if self.board[0] == 'x' or self.board[0] == 'o':
                win = True
        if self.board[2] == self.board[4] == self.board[6]:
            if self.board[2] == 'x' or self.board[2] == 'o':
                win = True
        
        if win:
            if self.user_name == self.lastmove:
                self.wins += 1
                return True
            else:
                self.losses += 1
                return False
        
    def boardIsFull(self) -> bool:
        """Checks if the board is full and updates the ties count.
        
        Returns:
            True if board is full
            False otherwise
        """
        dash_count = 9
        for i in self.board:
            if i != '-':
                dash_count -= 1
        if dash_count == 0:
            self.ties += 1
            return True
        return False
    
    def computeStats(self) -> str:
        """Compute and return the user's stats."""
        
        s = ("---GAME STATS---\n" + 
              "Your name: "+ self.user_name + "\n" + 
              "Opponent's name: " + self.opponent_name + "\n" +
              "Player with the last move: " + self.lastmove + "\n" +
              "Number of wins: " + str(self.wins) + "\n" +
              "Number of ties: " + str(self.ties) + "\n" +
              "Number of losses: " + str(self.losses) + "\n" +
              "Number of games played: " + str(self.games_played))
        return s
