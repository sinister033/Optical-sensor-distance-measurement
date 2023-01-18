# Optical-sensor-distance-measurement
This repository contains the code, working and the CAD model of the device made for measuring 2D- distance through an optical sensor.

![111](https://user-images.githubusercontent.com/97225407/213273361-aa819357-d7af-48d0-a6b4-c45acd32f8bc.jpeg)

**Idea**: The tools we use to measure distances between two points, whether they be rulers, tape measures, or even laser range finders, almost all have the same feature: only one axis of measurement. This means that taking more difficult readings can be challenging, particularly when determining the lengths of triangles without the aid of trigonometry. We developed a compact, portable device that allows us to rapidly and precisely take measurements in two axes using the internal circuitry of an Optical mouse.

## How does an Optical mouse Work?

> A tiny cutout that is located at the base of the computer mouse exposes a tiny camera with a resolution of just about 30 pixels by 30 pixels. After it takes a snapshot of the surface at a rate of 1500 frames per second, the current frame is compared to the previous one. By recording how far the image was shifted through counting the number of pixels, direction, position, and velocity can all be derived. 

![im1](https://user-images.githubusercontent.com/97225407/213274447-c90663fc-0d86-4f16-bad9-ef057c6efd8f.png)


> The optical mouse sends the events to the computer via a data packet. A data packet is a 3-byte packet that is sent to the computer every time the mouse state changes (the mouse moves or keys are pressed/released). 
The graph shown briefly depicts the data packets and respective key presses in the mouse, for more information, kindly refer to this [link](https://courses.cs.washington.edu/courses/cse477/00sp/projectwebs/groupb/PS2-mouse/mouse.html).

![im2](https://user-images.githubusercontent.com/97225407/213275017-41b01c92-4087-4091-a11e-d02ea5d99f49.png)


> We have used the same working principles to formulate a code that calculates the distance in any arbitrary 2-D direction.

## Requisite components:
> - An Optical Sensor ( Any optical mouse will do; the sensor's functionality is the only need. 
 
> - USB port (Here we are using a wireless mouse with a USB port already provided.)

![im3](https://user-images.githubusercontent.com/97225407/213275271-cf0d1151-7a91-437a-8120-17e267f9e275.jpg)


## Measurement modes:
> There are various modes in the code that we are implementing. First, you can choose from centimeters, inches, feet, and meters when deciding on the measuring unit. We can further customize the distance unit based on our needs. The distance can then be interpreted as either on the X- or Y-axis or both at the same time. Last but not least, each direction can be an absolute distance or can also consider the direction for lots of customization options.
## Programming the mouse:
> We are using the optical mouse framing property to calculate distance, which can be tracked using the mice input that comes to Ubuntu on /dev/input/mice. The first byte in the data packet is used to determine the mouse button pressed, and the next two bytes determine the distance moved in the X and Y directions, respectively. The device starts reading once the left button is pressed and keeps recording as long as the button is pressed. We obtain some value based on the amount of time the button was pressed, and upon dividing by the appropriate conversion number, we can get the final output as cm, mm, m, ft, or in. Since the optical mouse that we are using is 1000 DPI (dots per inch), we can divide 1000 by the final reading to get the readings in inches, and if we get the reading in inches, we can convert it to any measurement unit that we like.

