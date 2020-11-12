{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LET'S PLAY TIC TAC TOE\n",
      "Player 1 is X and has 1st turn\n",
      "PLayer 2 is O and is having second turn\n"
     ]
    }
   ],
   "source": [
    "ls=[0]*10\n",
    "turn=0\n",
    "s=['.']*10\n",
    "print(\"LET'S PLAY TIC TAC TOE\")\n",
    "print(\"Player 1 is X and has 1st turn\")\n",
    "print(\"PLayer 2 is O and is having second turn\")\n",
    "c=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player 1 turn\n",
      "9\n",
      " \n",
      "        \n",
      "     .  | . | X\n",
      "  ------|---|-------\n",
      "     .  | . | .\n",
      "  ------|---|-------\n",
      "     .  | . | .\n",
      "    \n",
      "    \n",
      "Player 2 turn\n",
      "4\n",
      " \n",
      "        \n",
      "     .  | . | X\n",
      "  ------|---|-------\n",
      "     O  | . | .\n",
      "  ------|---|-------\n",
      "     .  | . | .\n",
      "    \n",
      "    \n",
      "Player 1 turn\n",
      "3\n",
      " \n",
      "        \n",
      "     .  | . | X\n",
      "  ------|---|-------\n",
      "     O  | . | .\n",
      "  ------|---|-------\n",
      "     .  | . | X\n",
      "    \n",
      "    \n",
      "Player 2 turn\n",
      "6\n",
      " \n",
      "        \n",
      "     .  | . | X\n",
      "  ------|---|-------\n",
      "     O  | . | O\n",
      "  ------|---|-------\n",
      "     .  | . | X\n",
      "    \n",
      "    \n",
      "Player 1 turn\n",
      "1\n",
      " \n",
      "        \n",
      "     .  | . | X\n",
      "  ------|---|-------\n",
      "     O  | . | O\n",
      "  ------|---|-------\n",
      "     X  | . | X\n",
      "    \n",
      "    \n",
      "Player 2 turn\n",
      "5\n",
      " \n",
      "        \n",
      "     .  | . | X\n",
      "  ------|---|-------\n",
      "     O  | O | O\n",
      "  ------|---|-------\n",
      "     X  | . | X\n",
      "    \n",
      "    \n",
      "Player2 wins\n"
     ]
    }
   ],
   "source": [
    "while turn < 9:\n",
    "    if turn%2==0:\n",
    "        print(\"Player 1 turn\")\n",
    "        while 1:\n",
    "            a=int(input())\n",
    "            \n",
    "        ls[a]=1\n",
    "        s[a]='X'\n",
    "        turn+=1\n",
    "    elif turn%2==1:\n",
    "        print(\"Player 2 turn\")\n",
    "        b=int(input())\n",
    "        ls[b]=2\n",
    "        s[b]='O'\n",
    "        turn+=1\n",
    "    print(f\"\"\" \n",
    "        \n",
    "     {s[7]}  | {s[8]} | {s[9]}\n",
    "  ------|---|-------\n",
    "     {s[4]}  | {s[5]} | {s[6]}\n",
    "  ------|---|-------\n",
    "     {s[1]}  | {s[2]} | {s[3]}\n",
    "    \n",
    "    \"\"\")\n",
    "    if (s[1]=='X'and s[2]=='X'and s[3]=='X')or(s[4]=='X'and s[5]=='X'and s[6]=='X')or(s[7]=='X'and s[8]=='X'and s[9]=='X')or(s[1]=='X'and s[4]=='X'and s[7]=='X')or(s[2]=='X'and s[5]=='X'and s[8]=='X')or(s[3]=='X'and s[6]=='X'and s[9]=='X')or(s[1]=='X'and s[5]=='X'and s[9]=='X')or(s[3]=='X'and s[5]=='X'and s[7]=='X'):\n",
    "        print(\"Player1 wins\")\n",
    "        c=1\n",
    "        break\n",
    "    elif (s[1]=='O'and s[2]=='O'and s[3]=='O')or(s[4]=='O'and s[5]=='O'and s[6]=='O')or(s[7]=='O'and s[8]=='O'and s[9]=='O')or(s[1]=='O'and s[4]=='O'and s[7]=='O')or(s[2]=='O'and s[5]=='O'and s[8]=='O')or(s[3]=='O'and s[6]=='O'and s[9]=='O')or(s[1]=='O'and s[5]=='O'and s[9]=='O')or(s[3]=='O'and s[5]=='O'and s[7]=='O'):\n",
    "        print(\"Player2 wins\")\n",
    "        c=1\n",
    "        break\n",
    "if c==0:\n",
    "    print(\"No one wins\")\n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
