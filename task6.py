import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from PIL import Image, ImageTk
import random

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.gold = 0
        self.inventory = {"Potion": 2}

    def is_alive(self):
        return self.hp > 0

    def heal(self):
        if self.inventory["Potion"] > 0:
            self.hp = min(self.max_hp, self.hp + 30)
            self.inventory["Potion"] -= 1
            return True
        return False

class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG Adventure")

        # Load images
        self.player_img = ImageTk.PhotoImage(Image.open("player.png").resize((120, 120)))
        self.enemy_img = ImageTk.PhotoImage(Image.open("enemy.png").resize((120,120)))

        self.player = Character("Hero", 100, 20, 5)
        self.enemy = self.generate_enemy()

        # Frames
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(pady=5)

        self.player_frame = tk.Frame(self.top_frame)
        self.player_frame.pack(side=tk.LEFT, padx=20)

        self.enemy_frame = tk.Frame(self.top_frame)
        self.enemy_frame.pack(side=tk.RIGHT, padx=20)

        # Player display
        tk.Label(self.player_frame, text="Player", font=("Arial", 12, "bold")).pack()
        tk.Label(self.player_frame, image=self.player_img).pack()
        self.player_hp = ttk.Progressbar(self.player_frame, length=120, maximum=self.player.max_hp)
        self.player_hp.pack(pady=5)
        self.player_hp['value'] = self.player.hp
        self.player_stats = tk.Label(self.player_frame, text=self.get_player_stats(), font=("Arial", 10))
        self.player_stats.pack()

        # Enemy display
        tk.Label(self.enemy_frame, text="Enemy", font=("Arial", 12, "bold")).pack()
        tk.Label(self.enemy_frame, image=self.enemy_img).pack()
        self.enemy_hp = ttk.Progressbar(self.enemy_frame, length=120, maximum=self.enemy.max_hp)
        self.enemy_hp.pack(pady=5)
        self.enemy_hp['value'] = self.enemy.hp
        self.enemy_stats = tk.Label(self.enemy_frame, text=self.get_enemy_stats(), font=("Arial", 10))
        self.enemy_stats.pack()

        # Info label
        self.info_label = tk.Label(root, text="Click Attack to fight or Use Potion to heal.", font=("Arial", 12))
        self.info_label.pack(pady=5)

        # Log
        self.log = scrolledtext.ScrolledText(root, height=8, width=50, state=tk.DISABLED, font=("Arial", 11))
        self.log.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        self.attack_button = tk.Button(btn_frame, text="Attack", width=12, command=self.attack)
        self.attack_button.grid(row=0, column=0, padx=5)
        self.heal_button = tk.Button(btn_frame, text="Use Potion", width=12, command=self.use_potion)
        self.heal_button.grid(row=0, column=1, padx=5)
        self.next_button = tk.Button(btn_frame, text="Next Enemy", width=12, command=self.next_enemy, state=tk.DISABLED)
        self.next_button.grid(row=0, column=2, padx=5)
        self.restart_button = tk.Button(btn_frame, text="Restart", width=12, command=self.restart_game)
        self.restart_button.grid(row=0, column=3, padx=5)

        self.log_message("Welcome to RPG Adventure!")
        self.log_message(f"A wild {self.enemy.name} appears!")

    def get_player_stats(self):
        return f"HP: {self.player.hp}/{self.player.max_hp} | Attack: {self.player.attack} | Defense: {self.player.defense} | Gold: {self.player.gold} | Potions: {self.player.inventory['Potion']}"

    def get_enemy_stats(self):
        return f"HP: {self.enemy.hp}/{self.enemy.max_hp} | Attack: {self.enemy.attack} | Defense: {self.enemy.defense}"

    def update_labels(self):
        self.player_stats.config(text=self.get_player_stats())
        self.enemy_stats.config(text=self.get_enemy_stats())
        self.player_hp['value'] = self.player.hp
        self.enemy_hp['value'] = self.enemy.hp

    def log_message(self, msg):
        self.log.config(state=tk.NORMAL)
        self.log.insert(tk.END, msg + "\n")
        self.log.config(state=tk.DISABLED)
        self.log.see(tk.END)

    def generate_enemy(self):
        hp = random.randint(40, 80)
        attack = random.randint(8, 15)
        defense = random.randint(2, 5)
        name = random.choice(["Goblin", "Orc", "Wolf", "Bandit"])
        return Character(name, hp, attack, defense)

    def attack(self):
        if not self.player.is_alive():
            messagebox.showinfo("Game Over", "You are dead! Press Restart.")
            return
        if not self.enemy.is_alive():
            self.log_message("Enemy already defeated! Click Next Enemy.")
            return

        # Player attack
        damage = max(0, self.player.attack - self.enemy.defense)
        self.enemy.hp -= damage
        self.log_message(f"You hit {self.enemy.name} for {damage} damage.")
        if not self.enemy.is_alive():
            earned = random.randint(10, 30)
            self.player.gold += earned
            self.enemy.hp = 0
            self.log_message(f"{self.enemy.name} defeated! You earned {earned} gold.")
            self.info_label.config(text="Enemy defeated! Click 'Next Enemy' to continue.")
            self.attack_button.config(state=tk.DISABLED)
            self.heal_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.NORMAL)
            self.update_labels()
            return

        # Enemy attack
        damage = max(0, self.enemy.attack - self.player.defense)
        self.player.hp -= damage
        self.log_message(f"{self.enemy.name} hits you for {damage} damage.")
        if self.player.hp <= 0:
            self.player.hp = 0
            self.log_message("You have been defeated!")
            self.info_label.config(text="You are dead! Press Restart.")
            self.attack_button.config(state=tk.DISABLED)
            self.heal_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)
        self.update_labels()

    def use_potion(self):
        if not self.player.is_alive():
            messagebox.showinfo("Game Over", "You can't heal when dead!")
            return
        if self.player.heal():
            self.log_message("You used a potion and restored 30 HP.")
        else:
            self.log_message("No potions left!")
        self.update_labels()

    def next_enemy(self):
        self.enemy = self.generate_enemy()
        self.log_message(f"A new enemy {self.enemy.name} appears!")
        self.info_label.config(text="New enemy appeared! Attack or Heal.")
        self.attack_button.config(state=tk.NORMAL)
        self.heal_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        self.update_labels()

    def restart_game(self):
        self.player = Character("Hero", 100, 20, 5)
        self.enemy = self.generate_enemy()
        self.log.config(state=tk.NORMAL)
        self.log.delete(1.0, tk.END)
        self.log.config(state=tk.DISABLED)
        self.log_message("Game restarted! New adventure begins.")
        self.log_message(f"A wild {self.enemy.name} appears!")
        self.info_label.config(text="Attack or Heal to fight enemy.")
        self.attack_button.config(state=tk.NORMAL)
        self.heal_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        self.update_labels()

if __name__ == "__main__":
    root = tk.Tk()
    game = RPGGame(root)
    root.mainloop()
