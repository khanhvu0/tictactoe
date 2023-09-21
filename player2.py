import socket
import tkinter as tk
from tkinter import font 
from gameboard import BoardClass

class PlayerUI2():
    """A class for the host of tic tac toe GUI"""
    
    def __init__(self) -> None:
        """Initialize BoardClass and tkinter UI setup"""
        self.player = BoardClass()
        self.canvas_setup()
        self.init_var()
        self.start_setup()
        self.label_setup()
        self.board_setup()
        self.create_quit_button()
        self.run_UI()
        
    def run_UI(self) -> None:
        """Run tkinter mainloop"""
        self.master.mainloop()
        
    def init_var(self) -> None:
        """Init tkinter variables"""
        self.turn = tk.StringVar()
        self.my_text = tk.StringVar(value="Enter connection info")
        self.stats = tk.StringVar()
    
    def canvas_setup(self) -> None:
        """Setup canvas"""
        self.master = tk.Tk()
        self.master.title("Tic Tac Toe - host(o)")
        self.master.geometry('500x800')
        self.master.configure(background='white')
   
    def start_setup(self) -> None:
        """Setup the connection and name fields"""
        self.start_frame = tk.Frame(self.master)
        self.start_frame.pack()
        
        label1 = tk.Label(self.start_frame, text='Host IP address:')
        label1.grid(row=0,column=0)
        self.input1 = tk.Entry(self.start_frame)
        self.input1.grid(row=0,column=1)
        
        label2 = tk.Label(self.start_frame, text='Port number:')
        label2.grid(row=1,column=0)
        self.input2 = tk.Entry(self.start_frame)
        self.input2.grid(row=1,column=1)
        
        self.connect_button = tk.Button(self.start_frame, text='Connect', command=self.connect)
        self.connect_button.grid(row=0,column=2,rowspan=2)
        
        label3 = tk.Label(self.start_frame, text='Username:')
        label3.grid(row=2,column=0)
        self.input3 = tk.Entry(self.start_frame, state="disabled")
        self.input3.grid(row=2,column=1)
        self.name_button = tk.Button(self.start_frame, text='Enter', command=self.send_name, state="disabled")
        self.name_button.grid(row=2,column=2)
        
    def label_setup(self) -> None:
        """Setup the label fields"""
        label_frame = tk.Frame(self.master)
        label_frame.pack(side='top',pady=10)
        self.label1 = tk.Label(label_frame, textvariable=self.my_text, font=("Arial Bold",20))
        self.label1.pack()
        self.turn_label = tk.Label(label_frame, textvariable=self.turn, font=("Arial Bold",20))
        self.turn_label.pack()
        
    def stats_setup(self) -> None:
        """Setup the stats field"""
        stats_frame = tk.Frame(self.master).pack()
        self.stats = tk.Label(stats_frame, textvariable=self.stats)
        self.stats.pack()
        
    def process_move(self, button:tk.Button) -> None:
        """Process the user's button click, check for winner, and send the move.

        Args:
            button: The game board buttons
        """
        self.client_socket.setblocking(True)
        if button["text"] == '':
            button.config(text='o')
            i = button.index
            self.board[i] = 'o'
            self.player.lastmove = self.player.user_name
            self.player.updateGameBoard(self)
            
            if self.player.isWinner() == True:
                self.turn.set("You Won!")
                self.master.update_idletasks()
                self.client_socket.send(str(i).encode())
                self.end_game()
                return
            elif self.player.boardIsFull():
                self.turn.set("It's a tie!")
                self.master.update_idletasks()
                self.client_socket.send(str(i).encode())
                self.end_game()
                return
            else:
                self.turn.set(self.player.opponent_name+"'s turn")
                self.master.update_idletasks()
                self.send_move(i)
        else:
            self.turn.set("Try again")
        
    def board_setup(self) -> None:
        """Set up the game board buttons"""
        
        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()
        self.board = ["-","-","-","-","-","-","-","-","-"]
        self.buttons = []
        my_font = font.Font(family='Arial bold', size=50)
        
        self.entry1 = tk.Button(master=self.board_frame, text='', font=my_font,
                                width=2, height=1, background='white', 
                                command=lambda: self.process_move(self.entry1), state="disabled")
        self.entry1.grid(row=0,column=0, padx=3, pady=3)
        self.entry1.index=0
        self.entry2 = tk.Button(master=self.board_frame, text='',font=my_font,
                                width=2, height=1, background='white',
                                command=lambda: self.process_move(self.entry2), state="disabled")
        self.entry2.grid(row=0,column=1, padx=3, pady=3)
        self.entry2.index=1
        self.entry3 = tk.Button(master=self.board_frame, text='',font=my_font,
                                width=2, height=1, background='white',
                                command=lambda: self.process_move(self.entry3), state="disabled")
        self.entry3.grid(row=0,column=2, padx=3, pady=3)
        self.entry3.index=2
        self.entry4 = tk.Button(master=self.board_frame, text='',font=my_font,
                                width=2, height=1, background='white',
                                command=lambda: self.process_move(self.entry4), state="disabled")
        self.entry4.grid(row=1,column=0, padx=3, pady=3)
        self.entry4.index=3
        self.entry5 = tk.Button(master=self.board_frame, text='',font=my_font,
                                width=2, height=1, background='white',
                                command=lambda: self.process_move(self.entry5), state="disabled")
        self.entry5.grid(row=1,column=1, padx=3, pady=3)
        self.entry5.index=4
        self.entry6 = tk.Button(master=self.board_frame, text='',font=my_font,
                                width=2, height=1, background='white',
                                command=lambda: self.process_move(self.entry6), state="disabled")
        self.entry6.grid(row=1,column=2, padx=3, pady=3)
        self.entry6.index=5
        self.entry7 = tk.Button(master=self.board_frame, text='',font=my_font,
                                width=2, height=1, background='white',
                                command=lambda: self.process_move(self.entry7), state="disabled")
        self.entry7.grid(row=2,column=0, padx=3, pady=3)
        self.entry7.index=6
        self.entry8 = tk.Button(master=self.board_frame, text='',font=my_font,
                                width=2, height=1, background='white',
                                command=lambda: self.process_move(self.entry8), state="disabled")
        self.entry8.grid(row=2,column=1, padx=3, pady=3)
        self.entry8.index=7
        self.entry9 = tk.Button(master=self.board_frame, text='', font=my_font,
                                width=2, height=1, background='white',
                                command=lambda: self.process_move(self.entry9), state="disabled")
        self.entry9.grid(row=2,column=2, padx=3, pady=3)
        self.entry9.index=8
        
        self.buttons.extend((self.entry1,self.entry2,self.entry3,self.entry4,self.entry5,self.entry6,self.entry7,self.entry8,self.entry9,))
    
    def end_game(self) -> None:
        """Wait for client to play again or end the game and handles it"""
        
        self.entry1.config(state="disabled")
        self.entry2.config(state="disabled")
        self.entry3.config(state="disabled")
        self.entry4.config(state="disabled")
        self.entry5.config(state="disabled")
        self.entry6.config(state="disabled")
        self.entry7.config(state="disabled")
        self.entry8.config(state="disabled")
        self.entry9.config(state="disabled")
        self.master.update_idletasks()
        
        while True:
            try:
                x = self.client_socket.recv(1024).decode()
                if str(x) == "Fun Times":
                    self.my_text.set("Game ended")
                    self.turn.set("")
                    self.stats.set(self.player.computeStats())
                    self.stats_setup()
                    self.master.update_idletasks()
                    break
                if str(x) == "Play Again":
                    self.my_text.set("Let's play again")
                    self.turn.set("")
                    self.replay()
                    break
            except:
                pass
            
    def create_quit_button(self) -> None:
        """Setup quit button"""
        quit_frame = tk.Frame(self.master)
        quit_frame.pack(side='bottom')
        self.quit_button = tk.Button(master=quit_frame, text='Quit',command=quit).pack()
        
    def quit(self) -> None:
        """Close socket and tkinter GUI"""
        self.client_socket.shutdown()
        self.client_socket.close()
        self.master.destroy()
   
     
    def connect(self) -> None:
        """Setup socket host and wait for incoming connections

        Raises:
            ValueError: Invalid port number
        """
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = self.input1.get()
            port = int(self.input2.get())
            if 0 > port > 65353:
                raise ValueError
            self.my_text.set('Waiting for a connection')
            self.master.update_idletasks()
            server_socket.bind((host,port))
            server_socket.listen()
            self.client_socket,client_address = server_socket.accept()
            self.connect_button.config(state="disabled")
            self.name_button.config(state="normal")
            self.input3.config(state='normal')
            self.my_text.set("Connection successful, enter username")
            self.master.update_idletasks()
        except:
            self.my_text.set("Invalid connection info")
            self.input2.delete(0, "end")
            self.input1.delete(0, "end")

    def send_name(self) -> None:
        """Check and send the user name and wait for client's name"""
        
        self.player.user_name = self.input3.get()
        if self.player.user_name.isalnum():
            self.player.makeBoard()
            self.player.updateGamesPlayed()
            self.client_socket.send(self.player.user_name.encode())
            self.turn.set("Name cannot have special characters")
            self.name_sent = False
            while True:
                if self.name_sent == False:
                    self.master.after(0, self.recv_name())
                else:
                    break
            
            self.entry1.config(state="normal")
            self.entry2.config(state="normal")
            self.entry3.config(state="normal")
            self.entry4.config(state="normal")
            self.entry5.config(state="normal")
            self.entry6.config(state="normal")
            self.entry7.config(state="normal")
            self.entry8.config(state="normal")
            self.entry9.config(state="normal")
        else:
            self.turn.set("Name cannot have special characters")
            self.input3.delete(0, "end")
        
    def recv_name(self) -> None:
        """Receive the client's name and wait for client's move"""
        
        try:
            name = self.client_socket.recv(1024).decode()
            self.name_sent = True
            self.player.opponent_name = name
            self.my_text.set("Let's play Tic Tac Toe with "+ str(name))
            self.turn.set(str(name)+"'s turn")
            self.name_button.config(state="disabled")
            self.connect_button.config(state="disabled")
            self.client_socket.setblocking(False)
            self.master.update_idletasks()
            self.move_sent = False
            
            while True:
                if self.move_sent == False:
                    self.master.after(0, self.recv_move())
                else:
                    self.client_socket.setblocking(False)
                    self.move_sent = False
                    break
        except:
            pass

    def send_move(self, i:int) -> None:
        """Send the user's move and wait for client's move

        Args:
            i: the user's move
        """
        self.master.update_idletasks()
        self.client_socket.send(str(i).encode())
        self.player.lastmove = self.player.user_name
        
        self.move_sent = False
        while True:
            if self.move_sent == False:
                self.master.after(0, self.recv_move())
            else:
                self.client_socket.setblocking(False)
                self.move_sent = False
                break

        
    def recv_move(self) -> None:
        """Receive the client's move and check for winner"""
        
        try:
            i = int(self.client_socket.recv(1024).decode())
            self.board[i] = 'x'
            self.buttons[i].config(text='x')
            self.player.updateGameBoard(self)
            self.player.lastmove = self.player.opponent_name
            self.move_sent = True
            self.replay_sent = True
            
            if self.player.isWinner() == False:
                self.client_socket.setblocking(False)
                self.turn.set("You Lost")
                self.master.update_idletasks()
                self.end_game()
            elif self.player.boardIsFull():
                self.turn.set("It's a tie!")
                self.master.update_idletasks()
                self.end_game()
            else:
                self.turn.set(self.player.user_name+"'s turn")
                self.master.update_idletasks()
        except:
            pass
        
    def replay(self) -> None:
        """Set up for when client wants to play again and wait for client's move"""
        
        self.player.updateGamesPlayed()
        self.player.resetGameBoard(self)
        self.board_frame.destroy()
        self.board_setup()
        self.entry1.config(state="normal")
        self.entry2.config(state="normal")
        self.entry3.config(state="normal")
        self.entry4.config(state="normal")
        self.entry5.config(state="normal")
        self.entry6.config(state="normal")
        self.entry7.config(state="normal")
        self.entry8.config(state="normal")
        self.entry9.config(state="normal")
        self.master.update_idletasks()
        self.client_socket.setblocking(False)

        self.replay_sent = False
        while True:
            try:
                if self.replay_sent == False:
                    self.master.after(0, self.recv_move())
                else:
                    self.client_socket.setblocking(False)
                    self.replay_sent = False
                    break
            except:
                pass


if __name__ == '__main__':
    PlayerUI2()