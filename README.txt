Chris Simmons
HW3

1. Bag of Words

To run: run bag_of_words_driver.py

Uses helper methods from bag_of_words.py


The large try,except areas ignore the attribute error, when navigating through directories
when ignored the process works fine

The runtimes for each process are printed when the process is finished:
The most lengthy processes are:
Kmeans -- ~104 sec
Creating the testing historgram -- ~500 sec (approx 8-9 minutes)

When matches are displayed,
the file path is printed on the left column
the corresponding directory is printed on the right column (which is the directory the image should match to)

However, all the files match to the trees:
Possibly because the all_train_hist 2D array (in the mapping function)
is not created as a 2D array, but as a single list.
I not sure how that could be considering how I am creating a list of lists (2D array) as all_train_hist
displayed below:

(from mapping in bag_of_words)
for key in train_hist:
        emp = []
        for j in train_hist[key]:
            emp.append(j)
        all_train_hist.append(emp)
        map[n] = key
        n += 1

2. Stereo Matching

To run the stereo matching: run alt_stereo_driver.py

The other files stereo_matching.py and stero_driver.py were created without my knowledge
of the fact that we are permitted to use cv2.matchTemplate.
The stereo_driver.py with the stereo_matching.py runs incredibly slow otherwise.


3. Projection Matrix (extra)

a.

solve for P = KR[[I3x3 - C]]
since P = Intrnsic Matrix (3x4 containing focal points and center points) * extrinsic (4x4 containing rotation and translation
matrix)

Solve for Intrinsic matrix :

focal length = 1072 pixels

center point = (500,390) = (ox,oy)

b.

Considering the rotation and translation of the camera:

The orientation should be the rotation of the camera
and the posistion should be the translation. Thus,
orientation is R, position is C

c.
Since a rotation matrix using homogeneous coordinates is represented as:

Rx = [1,0,0],[0, cos, -sin],[0,sin,cos] in the x plane

Rx would equal [1,0,0],[0, cos10, -sin10],[0,sin10,cos10]

d.

If we are solely translating the camera along the x-axis, only the x value
should by increased by 10 units while the others are maintained

C = [[35], [50],[0]]





