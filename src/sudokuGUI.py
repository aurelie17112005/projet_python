import tkinter as tk
from tkinter import messagebox
import random
from Sudoku import Sudoku
from Backtracking import Backtracking
from Grille import Grille

class SudokuGUI:
    def __init__(self, master, n=9):
        self.master = master
        self.master.title(f"Sudoku {n}x{n}")
        self.n = n

        # Crée une grille de 9x9 pour les cases de saisie
        self.entries = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.entries[i][j] = tk.Entry(self.master, width=5, font=('Arial', 18), justify='center')
                self.entries[i][j].grid(row=i, column=j)

        # Boutons pour résoudre et générer le Sudoku
        self.solve_button = tk.Button(self.master, text="Résoudre", command=self.solve)
        self.solve_button.grid(row=n, column=0, columnspan=4)

        self.generate_button = tk.Button(self.master, text="Générer", command=self.generate)
        self.generate_button.grid(row=n, column=5, columnspan=4)

    def get_grid(self):
        """Récupère la grille depuis les widgets Entry"""
        grid = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                value = self.entries[i][j].get()
                row.append(int(value) if value.isdigit() else 0)
            grid.append(row)
        return grid

    def set_grid(self, grid):
        """Met à jour la grille dans les widgets Entry"""
        for i in range(self.n):
            for j in range(self.n):
                value = grid[i][j]
                self.entries[i][j].delete(0, tk.END)
                if value != 0:
                    self.entries[i][j].insert(0, str(value))

    def solve(self):
        """Résout le Sudoku en utilisant le backtracking"""
        grid = self.get_grid()
        sudoku = Sudoku(self.n)
        sudoku.grille = grid
        backtracking = Backtracking(sudoku)
        if backtracking.backtracking():
            self.set_grid(sudoku.grille)
        else:
            messagebox.showerror("Erreur", "Aucune solution trouvée")

    def generate(self):
        """Génère un Sudoku valide avec des cases vides."""
        # Étape 1 : Résoudre le Sudoku (obtenir une grille complète valide)
        sudoku = Sudoku(self.n)
        sudoku.solve()

        # Étape 2 : Supprimer des cases pour rendre le Sudoku partiellement résolu
        holes = 40  # Nombre de cases à vider
        while holes > 0:
            row = random.randint(0, self.n - 1)
            col = random.randint(0, self.n - 1)

            # Ne pas effacer une case déjà vide
            if sudoku.grille[row][col] != 0:
                backup = sudoku.grille[row][col]
                sudoku.grille[row][col] = 0  # Effacer la case

                # Vérifier si le Sudoku a toujours une solution unique
                grid_copy = [row[:] for row in sudoku.grille]
                temp_sudoku = Sudoku(self.n)
                temp_sudoku.grille = grid_copy
                if temp_sudoku.solve():  # Vérifier qu'il existe une solution
                    holes -= 1
                else:
                    sudoku.grille[row][col] = backup  # Restaurer la case si pas de solution unique

        self.set_grid(sudoku.grille)


# Fonction principale pour exécuter l'application
def main():
    root = tk.Tk()
    sudoku_gui = SudokuGUI(root, n=9)  # Vous pouvez changer n pour tester différentes tailles (ex: 4 pour 4x4)
    root.mainloop()


if __name__ == "__main__":
    main()
