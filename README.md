# Skycolor
This is an attempt at estimating the color and light intensity given off by the sky at a certain location, for the whole day, every day in a year. 

This calculation allows for a visualization, in the form of an image, where the pixel color and intesity represent the skycolor, the X-axis represent days in the year and the Y-axis represent time of day. 

## Visualization
My inspiration for this was a similar representation (i believe in black and white) that i saw in a museum in Svalbard in 2018. In particular, the lattitude at Svalbard offers a sky view that has both all dark and all bright days as seen in the image below.

![Longyearbyen, Svalbard](/examples/skycolor_v1_svalbard_2022.png)

This is ofcourse very different from the sky view of a lattitude where human life is more common, such as in Rome...

![Rome, Italy](/examples/skycolor_v1_rome_2022.png)

## Other uses
The other thing i want to do with this is to use it for very long duration timelapses. If set up correctly, you could in theory estimate exposure settings for a camera based on the brightness of your surroundings. The sky brightness would be a significant factor in such an estimation. This could eliminate flickering from any auto-exposure settings and provide a nice transition from day to night by taking time and place into account. 

# Going forward
## First things first...
This is an idea... not a fully fleaged project. I just needed to get in up on github. It's just a slow and ugly script right now but I want to try to be more serious about these kinds of projects.

## Todos:
Theres lots of little things, youknow... 
- project structure
- linting and formatting
- making sure async does what its supposed to
- writing tests.....
- naming things

the list goes on.

## Ambition of the skycolor project
My main goal is to host a website that can produce the graph from clicking on a map. Easy!
To reach that goal, I presume that I would make a rest-api that will handle the request, taking in year and coordinates. Possibly also placenames and color preferences.
