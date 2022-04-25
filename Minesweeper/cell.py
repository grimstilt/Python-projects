from tkinter import Button
import random
import settings


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False) -> None:
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.x = x
        self.y = y

    # Appending objects to all
        Cell.all.append(self)

    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=10,
            height=4,
            # text=f'{self.x}, {self.y}',
        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-3>', self.right_click)
        self.cell_btn_obj = btn

    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.neighbours_mines_count() == 0:
                for cell_obj in self.neighbours():
                    cell_obj.show_cell()
            self.show_cell()

    def show_mine(self):
        self.cell_btn_obj.configure(bg='red')

    def get_cell_by_pos(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_cell(self):
        # count =  self.neighbours_count()
        self.cell_btn_obj.configure(text=self.neighbours_mines_count())
    
    def neighbours(self):
        surrounding_cells = [
            self.get_cell_by_pos(self.x - 1, self.y - 1),
            self.get_cell_by_pos(self.x - 1, self.y),
            self.get_cell_by_pos(self.x - 1, self.y + 1),
            self.get_cell_by_pos(self.x, self.y - 1),
            self.get_cell_by_pos(self.x, self.y + 1),
            self.get_cell_by_pos(self.x + 1, self.y - 1),
            self.get_cell_by_pos(self.x + 1, self.y),
            self.get_cell_by_pos(self.x + 1, self.y + 1),
        ]
        return surrounding_cells

    def neighbours_mines_count(self):
        count = 0
        for cell in self.neighbours():
            if cell.is_mine:
                count += 1
        return count

    def right_click(self, event):
        print(event)
        print('right click')

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for cell in picked_cells:
            cell.is_mine = True

    def __repr__(self) -> str:
        return f'Cell({self.x}, {self.y})'
