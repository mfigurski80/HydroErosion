# HydroErosion
Python model of rain eroding a landscape. Hydroerosion model places random 'drops' on terrain and moves the terrain based on their movement

## File Descriptions
### generateLandscape.py
Creates a 2x2 matrix describing height and bedrock, using perlin noise

### viewLandscape.py
Graphs given 2x2 matrix in 3D

### erodeLandscape.py
Performs Naive algorithm to erode given landscape, accounting for bedrock

## Results (so far):
Performed erosion on 300x200 terrain with 600,000 iterations (current maps)

Before: ![Before Erosion](/images/before2.png)

After: ![After Erosion](/images/after2.png)
