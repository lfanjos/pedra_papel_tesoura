import tkinter
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from random import choice
import time



class App:

    def __init__(self, root):
        self.root = root
        self.player_choice = None
        self.score = [0, 0]
        # setting title
        root.title("Pedra, Papel ou Tesoura")
        # setting window size
        width = 427
        height = 213
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_202 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_202["font"] = ft
        GLabel_202["fg"] = "#333333"
        GLabel_202["justify"] = "center"
        GLabel_202["text"] = "Jogador 1"
        GLabel_202.place(x=40, y=130, width=70, height=25)

        GLabel_290 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_290["font"] = ft
        GLabel_290["fg"] = "#333333"
        GLabel_290["justify"] = "center"
        GLabel_290["text"] = "Computador"
        GLabel_290.place(x=300, y=130, width=70, height=25)

        self.result_lbl = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.result_lbl["font"] = ft
        self.result_lbl["fg"] = "#333333"
        self.result_lbl["justify"] = "center"
        self.result_lbl["text"] = ""
        self.result_lbl.place(x=150, y=30, width=110, height=25)

        self.score_lbl = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.score_lbl["font"] = ft
        self.score_lbl["fg"] = "#333333"
        self.score_lbl["justify"] = "center"
        self.score_lbl["text"] = "Placar"
        self.score_lbl.place(x=280, y=160, width=110, height=20)

        self.score_count_lbl = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.score_count_lbl["font"] = ft
        self.score_count_lbl["fg"] = "#333333"
        self.score_count_lbl["justify"] = "center"
        self.score_count_lbl["text"] = "J - 0 / CPU - 0"
        self.score_count_lbl.place(x=280, y=175, width=110, height=20)

        GRadio_695 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_695["font"] = ft
        GRadio_695["fg"] = "#333333"
        GRadio_695["justify"] = "center"
        GRadio_695["text"] = "Pedra"
        GRadio_695.place(x=160, y=60, width=85, height=25)
        GRadio_695["value"] = "pedra"
        GRadio_695["command"] = self.GRadio_695_command

        GRadio_847 = tk.Radiobutton(root)
        GRadio_847["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=10)
        GRadio_847["font"] = ft
        GRadio_847["fg"] = "#333333"
        GRadio_847["justify"] = "center"
        GRadio_847["text"] = "Papel"
        GRadio_847.place(x=160, y=90, width=85, height=25)
        GRadio_847["value"] = "papel"
        GRadio_847["command"] = self.GRadio_847_command
        GRadio_847.invoke()

        GRadio_929 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_929["font"] = ft
        GRadio_929["fg"] = "#333333"
        GRadio_929["justify"] = "center"
        GRadio_929["text"] = "Tesoura"
        GRadio_929.place(x=170, y=120, width=79, height=30)
        GRadio_929["value"] = "tesoura"
        GRadio_929["command"] = self.GRadio_929_command

        self.GButton_314 = tk.Button(root)
        self.GButton_314["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.GButton_314["font"] = ft
        self.GButton_314["fg"] = "#000000"
        self.GButton_314["justify"] = "center"
        self.GButton_314["text"] = "Jogar"
        self.GButton_314.place(x=170, y=170, width=70, height=25)
        self.GButton_314["command"] = self.GButton_314_command

        image1 = Image.open("paper.png")
        image1 = image1.resize((150, 150), Image.ANTIALIAS)
        self.choice = "paper"
        self.player1_photo = ImageTk.PhotoImage(image1)
        self.img_lbl = tkinter.Label(image=self.player1_photo)
        self.img_lbl.image = self.player1_photo
        self.img_lbl.place(x=25, y=30, width=100, height=100)

        image2 = Image.open("rock.png")
        image2 = image2.resize((150, 150), Image.ANTIALIAS)
        self.choice = "paper"
        self.computer_photo = ImageTk.PhotoImage(image2)
        self.cpu_img_lbl = tkinter.Label(image=self.computer_photo)
        self.cpu_img_lbl.image = self.computer_photo
        self.cpu_img_lbl.place(x=280, y=30, width=100, height=100)

    def change_photo(self, name, iscpu=False):
        if iscpu:
            self.choice = name
            self.computer_photo = ImageTk.PhotoImage(Image.open(f"{name}.png"))
            self.cpu_img_lbl = tkinter.Label(image=self.computer_photo)
            self.cpu_img_lbl.image = self.computer_photo
            self.cpu_img_lbl.place(x=280, y=30, width=100, height=100)
        else:
            self.choice = name
            self.player1_photo = ImageTk.PhotoImage(Image.open(f"{name}.png"))
            self.img_lbl = tkinter.Label(image=self.player1_photo)
            self.img_lbl.image = self.player1_photo
            self.img_lbl.place(x=25, y=30, width=100, height=100)

    def GRadio_695_command(self):
        self.change_photo('rock')
        self.player_choice = 'rock'

    def GRadio_847_command(self):
        self.change_photo('paper')
        self.player_choice = 'paper'

    def GRadio_929_command(self):
        self.change_photo('scissors')
        self.player_choice = 'scissors'

    def GButton_314_command(self):
        self.GButton_314['state'] = 'disabled'
        self.result_lbl['text'] = ''
        cpu_choice = self.computer_play()
        result = self.show_result(cpu_choice, self.player_choice)
        self.result_lbl['text'] = result
        self.count_score(result)
        self.GButton_314['state'] = 'active'

    def computer_play(self):
        opts = ['rock', 'paper', 'scissors']
        chosen = choice(opts)
        t_end = time.time() + 3
        while time.time() < t_end:
            self.change_photo(choice(opts), True)
            self.root.update()
            time.sleep(0.05)
        self.change_photo(chosen, True)

        return chosen

    def show_result(self, cpu, player):
        if player == 'rock':
            if cpu == 'rock':
                result = 'Empate.'
            elif cpu == 'paper':
                result = "Você perdeu :("
            else:
                result = "Você ganhou!"
        elif player == 'paper':
            if cpu == 'rock':
                result = 'Você ganhou!'
            elif cpu == 'paper':
                result = "Empate."
            else:
                result = "Você perdeu :("
        else:
            if cpu == 'rock':
                result = 'Você perdeu :('
            elif cpu == 'paper':
                result = "Você ganhou!"
            else:
                result = "Empate."
        return result

    def count_score(self, result):
        self.score[0] += 1 if result == 'Você ganhou!' else 0
        self.score[1] += 1 if result == 'Você perdeu :(' else 0
        self.score_count_lbl['text'] = f'J - {self.score[0]} / CPU - {self.score[1]}'

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
