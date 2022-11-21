'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade
arcade.open_window(700,700,"Carter Sousa")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
# background
k=((200,200),(200,500),(500,500),(500,200))
arcade.draw_polygon_filled(k,(97,16,86))
j=((100,0),(700,0),(700,600))
arcade.draw_polygon_filled(j,(110,22,98))
i=((600,700),(0,700),(0,100))
arcade.draw_polygon_filled(i,(110,25,98))
h=((0,700),(200,700),(0,0),(200,0))
arcade.draw_polygon_filled(h,(112,29,101))
g=((700,700),(0,700),(0,500),(700,500))
arcade.draw_polygon_filled(g,(115,33,104))
f=((500,0),(700,0),(700,700),(500,700))
arcade.draw_polygon_filled(f,(117,38,107))
e=((200,0),(200,200),(700,200),(700,0))
arcade.draw_polygon_filled(e,(122,44,112))
d=((0,700),(200,0),(0,0))
arcade.draw_polygon_filled(d,(130,51,119))
c=((0,700),(700,700),(0,500))
arcade.draw_polygon_filled(c,(138,57,127))
b=((700,0),(700,700),(500,700))
arcade.draw_polygon_filled(b,(145,67,135))
a=((0,0),(700,0),(700,200))
arcade.draw_polygon_filled(a,(158,77,147))
# Robe
arcade.draw_rectangle_filled(350,100,200,200,(18,17,56))
arcade.draw_arc_filled(350,150,200,600,(37,34,94),45,135)
arcade.draw_arc_filled(350,150,200,400,(37,34,94),45,135,45)
arcade.draw_arc_filled(350,150,200,400,(37,34,94),45,135,315)
arcade.draw_rectangle_filled(350,280,220,55,(37,34,94))
l=((275,250),(200,280),(125,50),(225,25))
arcade.draw_polygon_filled(l,(37,34,94))
m=((425,250),(500,280),(575,50),(475,25))
arcade.draw_polygon_filled(m,(37,34,94))
arcade.draw_triangle_filled(259,181,270,225,350,150,(25,23,71))
arcade.draw_triangle_filled(441,181,430,225,350,150,(25,23,71))
arcade.draw_triangle_filled(225,25,125,50,270,225,(25,23,71))
arcade.draw_triangle_filled(475,25,575,50,430,225,(25,23,71))
arcade.draw_ellipse_filled(175,37.5,103,25,(20,20,20),15)
arcade.draw_ellipse_filled(525,37.5,103,25,(20,20,20),345)
arcade.draw_triangle_filled(300,350,350,250,400,350,(25,23,71))
arcade.draw_arc_filled(350,350,100,150,(25,23,71),0,180)
arcade.draw_ellipse_filled(350,360,100,100,(20,20,20))
# red eyes
arcade.draw_ellipse_filled(325,375,20,20,(200,200,200))
arcade.draw_ellipse_filled(325,375,5,5,(200,0,0))
arcade.draw_ellipse_filled(375,375,20,20,(200,200,200))
arcade.draw_ellipse_filled(375,375,13,3,(200,0,0),45)
arcade.draw_ellipse_filled(375,375,13,3,(200,0,0),-45)
# sharp teeth
arcade.draw_arc_filled(315,355,20,20,(200,200,200),250,290,320)
arcade.draw_arc_filled(315,345,20,20,(200,200,200),70,110,-25)
arcade.draw_arc_filled(323,351,20,20,(200,200,200),250,290,345)
arcade.draw_arc_filled(326,341,20,20,(200,200,200),70,110,-15)
arcade.draw_arc_filled(334,349,20,20,(200,200,200),250,290,355)
arcade.draw_arc_filled(339,339,20,20,(200,200,200),70,110,-5)
arcade.draw_arc_filled(345,347,20,20,(200,200,200),250,290,360)#middle tooth
arcade.draw_arc_filled(351,339,20,20,(200,200,200),70,110,5)
arcade.draw_arc_filled(356,349,20,20,(200,200,200),250,290,5)
arcade.draw_arc_filled(364,341,20,20,(200,200,200),70,110,15)
arcade.draw_arc_filled(367,351,20,20,(200,200,200),250,290,15)
arcade.draw_arc_filled(375,345,20,20,(200,200,200),70,110,25)
arcade.draw_arc_filled(375,355,20,20,(200,200,200),250,290,40)
# floating green circles
Y=0
for i in range(11):
    arcade.draw_circle_filled(105,Y,10,(173,219,22))
    arcade.draw_circle_filled(595,Y,10,(173,219,22))
    Y+=70
X=0
for i in range(11):
    arcade.draw_circle_filled(X,600,10,(173,219,22))
    X+=70
# skull
arcade.draw_circle_filled(350,600,75,(200,200,200))
arcade.draw_circle_outline(350,600,75,(0,0,0,),2)
arcade.draw_ellipse_filled(290,600,30,60,(175,175,175))
arcade.draw_ellipse_filled(410,600,30,60,(175,175,175))
arcade.draw_circle_outline(350,600,75,(0,0,0,),2)
arcade.draw_rectangle_filled(350,560,140,20,(115,33,104))
                                                                      # middle
n=((310,620),(290,580),(270,570),(290,560),(300,560),(310,540),(310,520),(390,520),(390,540),(400,560),(410,560),(430,570),(410,580),(390,620))
arcade.draw_polygon_filled(n,(200,200,200))
arcade.draw_line(310,620,290,580,(0,0,0),2)
arcade.draw_line(290,580,270,570,(0,0,0),2)
arcade.draw_line(270,570,290,560,(0,0,0),2)
arcade.draw_line(290,560,300,560,(0,0,0),2)
arcade.draw_line(300,560,310,540,(0,0,0),2)
arcade.draw_line(310,540,310,520,(0,0,0),2)
arcade.draw_line(310,520,390,520,(0,0,0),2)
arcade.draw_line(390,520,390,540,(0,0,0),2)
arcade.draw_line(390,540,400,560,(0,0,0),2)
arcade.draw_line(400,560,410,560,(0,0,0),2)
arcade.draw_line(410,560,430,570,(0,0,0),2)
arcade.draw_line(430,570,410,580,(0,0,0),2)
arcade.draw_line(410,580,390,620,(0,0,0),2)
o=((293,560),(297,560),(305,510),(310,510),(310,520),(390,520),(390,510),(395,510),(403,560),(407,560),(402,500),(380,480),(320,480),(298,500),(293,560))
arcade.draw_polygon_filled(o,(200,200,200))
arcade.draw_polygon_outline(o,(0,0,0,),2)
teeth=318
for i in range(9):
    arcade.draw_line(teeth,510,teeth,530,(0,0,0),2)
    teeth+=8
p=((335,545),(340,540),(347,540),(350,542),(353,540),(360,540),(365,545),(355,580),(345,580))
arcade.draw_polygon_filled(p,(0,0,0))
arcade.draw_circle_filled(320,580,20,(0,0,0))
arcade.draw_ellipse_filled(320,580,5,25,(173,219,22),45)
arcade.draw_ellipse_filled(320,580,5,25,(173,219,22),-45)
arcade.draw_circle_filled(380,580,20,(0,0,0))
arcade.draw_circle_filled(380,580,4,(173,219,22))
q=((297,560),(300,560),(310,540),(310,510),(305,510))
arcade.draw_polygon_filled(q,(115,33,104))
arcade.draw_polygon_outline(q,(0,0,0),2)
r=((403,560),(400,560),(390,540),(390,510,),(395,510))
arcade.draw_polygon_filled(r,(115,33,104))
arcade.draw_polygon_outline(r,(0,0,0),2)
arcade.finish_render()
arcade.run()



