The Battle Ship Game
====================
   

Battle Ship is a game played by both players setting up his/her ship at a certain coordinate. This ship is two blocks
long and can either be placed vertically or horizontally. The other player, in this case a custom AI, guesses to try and locate the other players ship. Once the player has located one of the ship's blocks, he must find the second. The
second block could be on any of the first block's 4 sides. The AI knows this, and will use this information.

Hints
=====
- Guessing the same coordinate twice will lose you a turn.
- Always guess around the first block.
- The AI doesn't have a guessing pattern (though this is planned). Use this to your advantage.
 
Running The Game
================

###**Mac**

In Terminal, type the following:
```
cd /path/to/this/folder/
```
Then,
```
python battle.py
```

###**Windows**

In Command Prompt, type the following:
```
cd C:\path\to\this\folder\
```
Then,
```
python battle.py
```
