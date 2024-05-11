{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ed4a9388",
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import clear_output\n",
    "\n",
    "# displaying the game board\n",
    "\n",
    "def display_board(board):\n",
    "    clear_output()\n",
    "    print(board[1] + '|' + board[2] + '|' + board[3])\n",
    "    print('*****')\n",
    "    print(board[4] + '|' + board[5] + '|' + board[6])\n",
    "    print('*****')\n",
    "    print(board[7] + '|' + board[8] + '|' + board[9])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "130b798e",
   "metadata": {},
   "outputs": [],
   "source": [
    "board = [' ']*10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "20d04222",
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_input():\n",
    "    \n",
    "    \"\"\"\n",
    "    OUTPUT = (PLAYER 1 MARKER, PLAYER 2 MARKER)\n",
    "    \"\"\"\n",
    "    \n",
    "    marker = ''\n",
    "    \n",
    "    # Ask player to choose X or O\n",
    "    \n",
    "    while marker != 'X' and marker != 'O':\n",
    "        marker = input('Player 1, Choose X or O: ').upper()\n",
    "    \n",
    "    if marker == 'X':\n",
    "        return ('X', 'O')\n",
    "    else:\n",
    "        return ('O', 'X')  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1830cd29",
   "metadata": {},
   "outputs": [],
   "source": [
    "def board_update(board, marker, position):\n",
    "    board[position] = marker"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a861a17e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def win_check(board, mark):\n",
    "    \n",
    "    #checking all the possible results to win\n",
    "    return ((board[7] == board[8] ==  board[9] == mark) or # across the top\n",
    "    (board[4] == board[5] == board[6] == mark) or # across the middle\n",
    "    (board[1] == board[2] == board[3] == mark) or # across the bottom\n",
    "    (board[7] == board[4] == board[1] == mark) or # down the middle\n",
    "    (board[8] == board[5] == board[2] == mark) or # down the middle\n",
    "    (board[9] == board[6] == board[3] == mark) or # down the right side\n",
    "    (board[7] == board[5] == board[3] == mark) or # diagonal\n",
    "    (board[9] == board[5] == board[1] == mark)) # diagonal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "134c9516",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "# using random to decide who goes first\n",
    "\n",
    "def first_player():\n",
    "    if random.randint(0, 1) == 0:\n",
    "        return 'Player 2'\n",
    "    else:\n",
    "        return 'Player 1'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ccfd987f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_space(board, position):\n",
    "    \n",
    "    return board[position] == ' '"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f750c347",
   "metadata": {},
   "outputs": [],
   "source": [
    "def full_board_check(board):\n",
    "    \n",
    "    for x in range(1,10):\n",
    "        if check_space(board, x):\n",
    "            return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "33cf0408",
   "metadata": {},
   "outputs": [],
   "source": [
    "def position_choice(board):\n",
    "    \n",
    "    position = 0\n",
    "    \n",
    "    board_free = False\n",
    "    \n",
    "    acceptable_value = range(1, 10)\n",
    "    \n",
    "    while position not in acceptable_value and not board_free:\n",
    "        position = input(\"Please enter the number of board choice: \")            \n",
    "            \n",
    "        if position.isdigit():\n",
    "            position = int(position)\n",
    "            if position in acceptable_value:\n",
    "                board_free = check_space(board, position)\n",
    "        if not board_free:\n",
    "            position = 0\n",
    "    \n",
    "    return position"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c6378216",
   "metadata": {},
   "outputs": [],
   "source": [
    "def replay():\n",
    "\n",
    "    choice = ' '\n",
    "    while choice != 'Y' or choice != 'N':\n",
    "        choice = input('Do you want to play again? Type Y or N')\n",
    "        \n",
    "        if choice == 'Y':\n",
    "            return True\n",
    "        elif choice == 'N':\n",
    "            return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d5f34538",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " | |O\n",
      "*****\n",
      "X|O|X\n",
      "*****\n",
      "O|X|O\n",
      "Player 2 is Winner, Congratulations!\n",
      "Do you want to play again? Type Y or N5\n",
      "Do you want to play again? Type Y or NN\n"
     ]
    }
   ],
   "source": [
    "print('Welcome to Tic Tac Toe!')\n",
    "\n",
    "game_on = True\n",
    "\n",
    "while True:\n",
    "    # rest the board\n",
    "    board = [' ']*10\n",
    "    player1_marker, player2_marker = player_input()\n",
    "    turn = first_player()\n",
    "    print(turn + ' will go first.')\n",
    "\n",
    "    play_game = input('Are you ready to play? Enter Yes or No.')\n",
    "    \n",
    "    if play_game.lower()[0] == 'y':\n",
    "        game_on = True\n",
    "    else:\n",
    "        game_on = False\n",
    "        \n",
    "    while game_on:\n",
    "    \n",
    "        #Player 1 Turn\n",
    "        if turn == 'Player 1':\n",
    "            \n",
    "            # Show the board\n",
    "            display_board(board)\n",
    "            \n",
    "            # Choose a position\n",
    "            position = position_choice(board)\n",
    "            \n",
    "            #Update the board\n",
    "            board_update(board, player1_marker, position)\n",
    "\n",
    "            if full_board_check(board):\n",
    "                game_on = False\n",
    "                break\n",
    "\n",
    "            # check if player has won or the game is tied\n",
    "            if win_check(board, player1_marker):\n",
    "                display_board(board)\n",
    "                print(\"Player 1 is Winner, Congratulations!\")\n",
    "                game_on = False\n",
    "            else:\n",
    "                if full_board_check(board):\n",
    "                    display_board(board)\n",
    "                    print('The game is a draw!')\n",
    "                    break\n",
    "                \n",
    "                # Game continues, turn moves to player 2\n",
    "                else:\n",
    "                    turn = 'Player 2'\n",
    "            \n",
    "        # Player2's turn.\n",
    "        else:\n",
    "            display_board(board)\n",
    "            position = position_choice(board)\n",
    "            board_update(board, player2_marker, position)\n",
    "\n",
    "            if win_check(board, player2_marker):\n",
    "                display_board(board)\n",
    "                print(\"Player 2 is Winner, Congratulations!\")\n",
    "                game_on = False\n",
    "            else:\n",
    "                if full_board_check(board):\n",
    "                    display_board(board)\n",
    "                    print('The game is a draw!')\n",
    "                    break\n",
    "                else:\n",
    "                    turn = 'Player 1'\n",
    "\n",
    "    if not replay():\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b884ed0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "864d92a6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
