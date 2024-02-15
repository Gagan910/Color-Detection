# Python_Project
Three different colors Red, Green and  Blue are being tracked by utilizing the fundamentals of computer vision. After successful compilation when  we execute the code a window redirect to the image displayed on it whose path is given as an argument. Additionally, we obtain the color name of the pixel along with the composition of three different colors  red, blue and green values. 

### METHODOLOGY 

#### Image capture 

The first step is to fetch a high-quality image with resolution. To load an image from a file we  useCv2.imread(). Image should be in the working directory or the full path of the image should be given.  Img=cv2.imread(img path)Extraction of RGB.  
#### Extraction of RGB Colors

In this phase, the 3 layered colors are extracted from the input image. All the color images on screens  such as televisions, computer, monitors, laptops and mobile screens are produced by the combination of  Red, Green and Blue light. Each primary color takes an intensive value 0 (lowest) to 255 (highest).  When mixing 3 primary colors at different intensity levels a variety of colors are produced. For Example: If  the intensity value of the primary colors is 0, this linear combination corresponds to black. If the intensity  value of the primary colors is 1, this linear combination corresponds to white. 

Index=[ "color",  "color_name", "hex", "R", "G", "B"].

#### Calculate minimum distance from coordinates

The minimum distance is calculated by considering moving towards the origin point from all colors to get  the most matching color. The pandas library serves as an important utility to perform various operations on  comma- seperated values like pd.read _csv() reads the csv file and loads it into the pandas data frame. D = abs(R-int(csv.loc[i ,"R"])) + abs (G-int(csv.loc[i ,"G"])) + abs (B- int (csv.loc [i ,"B"]))Image Display  with Shades of Color: The rectangle window is used to display the image with shades of color.  After the double-click is triggered, the RGB values and color name is updated. To display an image  Cv2.imshow () method is used. By using cv2.rectangle and cv2.putText () functions, the color name and its  intensity level can be obtained. text=getColorName(r,g,b) + 'R='+str(r) + 'G='+str(g) + 'B=' +str(b).

### AAPPLICATION
  * It is helpful in recognizing colors and in robotics.
  * One of the applications of color detection computer vision is in driver less cars.
  * This system is useful in detecting traffic and vehicle back lights and takes decision to stop, start and continue driving.
  * This also have much application in industry to pick and place different colored object by the robotic arm.
  * Color detection is also used as a tool in various image editing and drawing apps.
  
### CONCLUSION
 In this project we defined to get the required color field from an RGB image. In this various steps are  implemented using the openCv platform. The main positive point of this method is its color differentiation  of a mono color. In the future scope, the detection of the edge detection techniques has different other  applications like facial detection, color conversion for grayscale image etc. that can also be implemented. 
