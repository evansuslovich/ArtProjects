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

 5x5ft project with 1x1ft squares inside 
        

In my project. I want to create a descending color pallete 
In 6x6 boxes. Ideally the top left corner will be warm and the bottom
right corner will be cold 

After that I am going to apply a layer of 3x3 black boxes in
random coordinate points 
"""


    



#class RedGreenBlue that takes in three parameters 
class RedGreenBlue:
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue

  def str(self):
    print("Red:", self.red, '\n' + "Green:", self.green, '\n' +  "Blue:", self.blue, '\n')



def createArray(colors, amount):
    interval = 255/amount
    for x in range(amount + 1):
        colors.append(RedGreenBlue((255-(x*interval)), 0, x*interval))

def printArray(colors):
    for i in range(len(colors)):
        colors[i].str()
    


colors = [] 
createArray(colors, 10)
printArray(colors)



        


   



    

 



