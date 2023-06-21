import turtle

# Draw the game board
def draw_board():
    turtle.penup()
    turtle.goto(-150, 150)
    turtle.pendown()
    turtle.forward(300)
    turtle.penup()
    turtle.goto(-150, 50)
    turtle.pendown()
    turtle.forward(300)
    turtle.penup()
    turtle.goto(-50, 250)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(300)
    turtle.penup()
    turtle.goto(50, 250)
    turtle.pendown()
    turtle.forward(300)

# Draw an X 
def draw_x(x, y):
    turtle.penup()
    turtle.goto(y * 100 - 120 , x * (-100) + 180)
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(y * 100 - 85, x * (-100) + 180)
    turtle.pendown()
    turtle.setheading(135)
    turtle.forward(50)

# Draw an O
def draw_o(x, y):
    turtle.penup()
    turtle.goto(y * 100 - 80, x * (-100) + 215)
    turtle.pendown()
    turtle.circle(25)

# Check if a player has won
def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Main game loop
def play_game():
    # Initialize the game board
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    players = ['X', 'O']
    turn = 0
    game_over = False
    
    # Draw the game board
    draw_board()
    
    # Main game loop
    while not game_over:
        player = players[turn % 2]
        x, y = turtle.textinput(f"{player}'s turn", "Enter x,y coordinates:").split(",")
        x, y = int(x), int(y)
        
        # Check if the chosen space is empty
        if board[x][y] != '':
            print("That space is already taken. Choose another one.")
            continue
        
        # Update the board and draw the appropriate symbol
        board[x][y] = player
        if player == 'X':
            draw_x(x , y )
        else:
            draw_o(x, y )
        
        # Check if the game is over
        if check_win(board, player):
            print(f"{player} wins!")
            game_over = True
        elif turn == 8:
            print("It's a tie!")
            game_over = True
        
        # Increment the turn counter
        turn += 1
    
    turtle.done()

# Start the game
play_game()
