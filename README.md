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

Start Page:  
![Start Page](demo.png)  
Demo Video:  
https://user-images.githubusercontent.com/40175039/204050898-9efa083e-a28d-4c83-983d-b90b10778d09.mp4  

![demo](https://user-images.githubusercontent.com/40175039/204050904-a979e511-494e-49ae-b091-68c5d9eece33.png)

[Ref 1] https://www.pygame.org/news  

