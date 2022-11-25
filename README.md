This is a simple game which simulates drone controls with gamepad.  
It uses Pygame to mimic 4 axis controls for yaw, throttle, roll and pitch.  

The biggest challenge is that pygame only supports 2D games, but it is  
required to control a drone with 4 axises and display the results.  
I use two 2D images, a top view and a rear view, of a drone icon to  
solve this issue.   

Environments:  
1. MS Windows 11  
2. Python 3.9.7  
3. Pygame 2.1.2 [Ref 1]  
4. Logitech Gamepad F310  

Game Controls:

Windows:
- Start: python dronesim.py
- Exit: ESC key

Gamepad (Mode 2):  
- Axis 0: Yaw: Left, Right  
- Axis 1: Throttle: Up, Down  
- Axis 2: Roll: Left, Right  
- Axis 3: Pitch: Up, Down  
- Axis 4: Speed: +10%  
- Axis 5: Reset

DroneSim GUI:
![Start Page](demo.png)
DroneSim Video:
![Video](demo.mp4)

[Ref 1] https://www.pygame.org/news

