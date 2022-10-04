# Skycolor

This is an attempt at estimating the color and light intensity given off by the sky at a certain location, for the whole day, every day in a year. 

This calculation allows for a visualization, in the form of an image, where the pixel color and intesity represent the skycolor, the X-axis represent days in the year and the Y-axis represent time of day. 

My inspiration for this was a similar representation (i believe in black and white) that i saw in a museum in Svalbard in 2018. In particular, the lattitude at Svalbard offers a sky view that has both all dark and all bright days as seen in the image below.

![Alt text](examples\skycolor_v1_svalbard_2022.png)

This is ofcourse very different from the sky view of a lattitude where human life is more common, such as in Rome...

![Alt Text](examples\skycolor_v1_rome_2022.png)

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
