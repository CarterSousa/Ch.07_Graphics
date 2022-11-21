'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''
import arcade
arcade.open_window(494,260,"My flag")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for i in range(10,270,40):
    arcade.draw_rectangle_filled(247,i,494,20,(191,10,48))
arcade.draw_rectangle_filled(98.6,190,197.6,140,(0,40,104))
for i in range(7,198,35):
    arcade.draw_text("*",i,235,arcade.color.WHITE,16)
for i in range(24,180,35):
    arcade.draw_text("*",i,221,arcade.color.WHITE,16)
for i in range(7,198,35):
    arcade.draw_text("*",i,207,arcade.color.WHITE,16)
for i in range(24,180,35):
    arcade.draw_text("*",i,193,arcade.color.WHITE,16)
for i in range(7,198,35):
    arcade.draw_text("*",i,179,arcade.color.WHITE,16)
for i in range(24,180,35):
    arcade.draw_text("*",i,165,arcade.color.WHITE,16)
for i in range(7,198,35):
    arcade.draw_text("*",i,151,arcade.color.WHITE,16)
for i in range(24, 180, 35):
    arcade.draw_text("*",i,137,arcade.color.WHITE,16)
for i in range(7,198,35):
    arcade.draw_text("*",i,123,arcade.color.WHITE,16)
arcade.finish_render()
arcade.run()