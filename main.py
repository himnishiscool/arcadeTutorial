import arcade

#Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (100, 0, 100)
PINK = (255, 0, 255)


#Window Setup
window = arcade.Window(1280, 720, "Tutorial")

#Game Class
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
    
    def on_draw(self):
        self.clear()

        #Circle
        arcade.draw_circle_filled(100, 100, 30, arcade.color.RED)
        arcade.draw_circle_outline(150, 150, 30, RED)

        #Rectangle
        arcade.draw_lbwh_rectangle_filled(250, 250, 100, 100, PURPLE)
        arcade.draw_lbwh_rectangle_outline(250, 50, 100, 100, BLUE)

        arcade.draw_lbwh_rectangle_filled(200, 200, 100, 100, BLUE)

        #Arc
        arcade.draw_arc_filled(500, 300, 100, 100, GREEN, 0, 90)
        arcade.draw_arc_outline(550, 350, 100, 100, GREEN, 0, 90)

        #Parabola
        arcade.draw_parabola_filled(250, 450, 300, 100, PINK)

        #Line
        arcade.draw_line(600, 600, 800, 650, CYAN, 2)

#Running Game
game = GameView()
window.show_view(game)
arcade.run()