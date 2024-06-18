import turtle

def main():

    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Gas")
    wn.setup(700,700)

    #com esta fet el mapa map
    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("white")
            self.penup()
            self.speed(0)

    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("blue")
            self.penup()
            self.speed(0)

        def go_up(self):
            #calcular el espai per mourese
        
            move_to_x =player.xcor()
            move_to_y =player.ycor() +24            
            
            #espais on hi ha pareds
            if (move_to_x, move_to_y)not in walls:
                self.goto(move_to_x, move_to_y)

        

        def go_down(self):
            move_to_x =player.xcor()
            move_to_y =player.ycor() -24
            if (move_to_x, move_to_y)not in walls:
                self.goto(move_to_x, move_to_y)

        
        def go_left(self):
            move_to_x =player.xcor() -24    
            move_to_y =player.ycor() 
            if (move_to_x, move_to_y)not in walls:
                self.goto(move_to_x, move_to_y)


        def go_right(self):
            move_to_x =player.xcor() +24
            move_to_y =player.ycor() 
            if (move_to_x, move_to_y)not in walls:
                self.goto(move_to_x, move_to_y) 
        


            
        


    #nivels de la llista
    levels = [""]

    #definir el primer nivell
    Level_1= [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX           XXXXXX",
    "X  XXXXXXX  XXXXXXX  XXXXXX",   
    "X       XX  XXXXXX      XXX",
    "X       XX  XXX         XXX",
    "XXXXXX  XX  XXXXXX   XXXXXX",
    "XXXXXX  XX     XXX   XXXXXX",
    "XXXXXX  XX     XXX   XXXXXX",
    "X   XXX     XXXXXXXXXXXXXXX",
    "X          XXXXXXXXXXXXXXXX",
    "X                      XXXX",
    "XXXXXXXXXXXXX      XXXX   X",
    "XXXXXXXXXXXXXXXX   XXXX   X",
    "XXX  XXXXXXXXXXX          X",
    "XXX                       X",
    "XXX           XXXXXXXXXXXXX",
    "XXXXXXXXXX   XXXXXXXXXXXXXX",
    "XXXXXXXXXX                X",
    "XX      XXXXXXXXXXX    XXXX",
    "XX      XXXXXXXXXXX    XXXX",
    "XXXX                      X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
    ]

    levels.append(Level_1)


    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level [y][x]
                screen_x = -288 + (x*24)
                screen_y = 288 - (y*24)
                #Representa el jugador
                if character == "P":
                        player.goto(screen_x, screen_y)

                #Representa les pareds
                if character == "X":
                        pen.goto(screen_x, screen_y)
                        pen.stamp()
                    #fer que el jugador no transpase les pareds
                        walls.append((screen_x, screen_y))
        

            
            
            
    pen = Pen()
    player = Player()

    #crear pareds per a posar limits i no pasar
    walls = []


    setup_maze(levels[1])
    print(walls)

    turtle.listen()
    turtle.onkey(player.go_left,"Left")
    turtle.onkey(player.go_right, "Right")
    turtle.onkey(player.go_down, "Down")
    turtle.onkey(player.go_up, "Up")
    wn.tracer(0)

    while True:
        wn.update() 
        

def pex3():
    main()