Author : Arun C
Description : Simple implementation of how spectral bisection graph partition to divide the given set of vertices into 2

In the code, the a blif file is converted to graphml and used in the code. It calculates the laplacian of the given set of vertices
From the Laplacian matrix, it essentially calculated the Eigen Value, and its corresponding Eigen Vectors.
The Eigen Values are arranged in ascending order, and the corresponding Eigen Vector to 2 smallest Eigen Value gives the partition details.
The elements in the corresponding Eigen Vector, the sign, positive or negative will reveal which partition the indexed vertice belong to.


How to run the code and get the output.

python graph.py

This will give you the second eigen value in the ascending order, Pick up the eigen vector corresponding to this eigen value, the polarity of the eigen vector values gives the partition indice of the vertices.
