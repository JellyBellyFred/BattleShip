The Battle Ship Game
====================
   

Battle Ship is a game played by both players setting up his/her ship at a certain coordinate or block. This ship is two blocks long and can either be placed vertically or horizontally. The other player, in this case a smart AI, guesses to try and locate the other player's ship. Once the player has located one of the ship's blocks, he must find the second. The second block could be on any of the first block's 4 sides. The AI knows this, and will use this information to its advantage.

Hints
=====
- Guessing the same block twice will lose you a turn.
- Always guess around the first found block.
- Your opponent is smart and has a strategy!
 
Running The Game
================

### Before We Start...

Download Python from:
```
http://python.org/
```
Now, install Python. You're all set! Procede to the following section for your OS.

### Mac / Linux

In Terminal, type the following:
```
cd /path/to/file/directory/
```
Then,
```
python battle.py
```
_For the best cosmetic result on a Mac, Control-Click the Terminal window and click Show Inspector. There, change the values of "Columns" to 179, and "Rows" to 53, or the largest your screen can handle._

_For the best cosmetic result on Linux, make sure the Terminal window is as large as it can be._

### Windows

In Command Prompt, type the following:
```
cd C:\path\to\file\directory\
```
Then,
```
python battle.py
```
_For the best cosmetic result on a Windows, make sure the Command Prompt window is as large as it can be._
