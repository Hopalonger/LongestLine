# Lake Trig Tool
# The point of this tool is to find the maximum distance across any two points
# of a body. This system operates using the input of points in the 1 Quadrent of
# a cordiante plane and trys every single combination possible
# Program Accepts tracks drawn with this tool: https://www.gpsvisualizer.com/draw/
# Export as txt file and all will be parsed
# Running the code: `python3 Main.py FILENAME.txt`
# Note to Math Teacher
# The only actual math is done at line 37 or where is says `Does the Actual processing`
# All of the stuff above that is just so it can interact with the files
import sys
import math
# Delcared Vars, Just leave them
Max = 0
MaxPoint1 = 0
MaxPoint2 = 0
XDis = 0
YDis = 0
Points = []
#Opens file
file = sys.argv[1]
print("Anylizing file: " + file)
f = open(file, "r")
lines = f.readlines()[1:]
for l in lines:
    line = str(l).split()
    if len(line) == 0:
        break
    Poi = str(line[1]) + "," + str(line[2])
    Points.append(Poi)
f.close()
print("Covereted File To Dataset")
# Converts Points to numbers
def Convert(string):
    li = list(string.split(","))
    return li
# Does the actual processing
for point in Points: #Says for every single point we have we will run the code below
    # Takes the "-14.87575,120.0303" and breaks it up into X1, and y1
    # x1 would equal -14.87575 and y1 would equal 120.0303
    P = Convert(point)
    x1 = float(P[0])
    y1 = float(P[1])

    for H in Points: # Now we compare this point to all points
        Z = Convert(H) #We convert the points into there x and y Componets like above
        x2 = float(Z[0])
        y2 = float(Z[1])

        x3 =  abs(x1 - x2) #Find the absloute value diffrence of X
        y3 = abs(y1 - y2) #Find the absloute value diffrence of Y
        hyp = math.sqrt((x3*x3) + (y3*y3)) # Run Pythageran Therom
    #    print(hyp * 69)
        if hyp > Max: # Check if the longest distance compared to the lognest previous one
            Max = hyp # if true set all of the values the end screen could need
            MaxPoint1 = str(x1) + "," + str(y1)
            MaxPoint2 = str(x2) + "," + str(y2)
            XDis = x3
            YDis = y3
# Once all of the points have been compared print the longest angels distace
print("Max Distance: " + str(Max * 69) + " (Miles)" )
print("X Distance: " + str(XDis * 69) + " (Miles)" )
print("Y Distance: "+ str(YDis * 69) + " (Miles)" )
print("Angle (Degrees): " + str(math.degrees(math.atan(XDis/YDis))))
print("Angle (Radians): " + str(math.atan(XDis/YDis)))
print("Between: " + MaxPoint1 + " And: " + MaxPoint2 + " Latatude / longitude")

# Summarized Math
# Get Point 1, Split it up into X and y Positions
# Get Point 2, Split into x and y positions
# Get Absoulte value diffrences between Point 1's X and Point 2's X
# Get Absoulte value diffrences between Point 1's Y and Point 2's Y
# Run Pythageran Therom Square Root((X-Dif * X-Dif) + (Y-Dif * Y-Dif))
# Check is this value larger than all other previous values
# if yes save, and keep going
# if no keep going
# When no Values left end program
#When finsihed print Max Distance and the points between
