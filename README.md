# EcuDebugCtrl
Server to control ECU reset and debugger on off state over raspberry pi http server and 2 servos

You have to have raspberry py and two servos to run this tiny server. 
The main idea is to orgaize debug PC for the remote acces.
Some procedures, which local person can do without thinking like quickly switch on and off the target, 
or debugger or the power supply become just impossible if trying to work remotely.

I have tried to solve this issue with non-intrusive methods, i.e. I havend disassembled debugger to 
include any ralais, but used servos with some physical mount to enable physically switch debugger on and off.

You can use this work as a jump off to make you own remote station or something else.
