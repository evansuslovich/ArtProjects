

""" Image Processing 
 - OpenCV 
 - Mahotas
 - Scikit-Image
 - Pgmagick
 - SimpleITK
 My plan for this project is I want to sketch my art using my programming
 ability rather than my brain -> my hypothesis is that I can be more creative 
 with code rather than intuition. 
 
 Can my code surpass my artistic ability and intuiton 


 Project 

 6x6ft project with 1x1ft squares inside 
        

In my project. I want to create a descending color pallete 
In 6x6 boxes. Ideally the top left corner will be warm and the bottom
right corner will be cold 

After that I am going to apply a layer of 3x3 black boxes in
random coordinate points 
"""


def main(): 
    #store in 36 variables the information of rgb values 
    p1 = RedGreenBlue(200, 123, 254) # example of an rgb value of 200,123,254

    print(p1.blue)
    print(p1.red)
    print(p1.green)


#class RedGreenBlue that takes in three parameters 
class RedGreenBlue:
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue



main()