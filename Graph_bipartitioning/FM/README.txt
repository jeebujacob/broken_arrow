This is a readme for the code FM.py
Author : Jeebu Jacob Thomas


The code bipartitions the set of eight nodes. User is not provided discretion to add or delete any nodes, or input nodes
The code basically works on an AREA CONSTRAINT, which is set as (3,5) which means the number of vertices in any partition should be in between the range 3-5. Owing to this we fix the vertices to be eight in number, But the user can change the number of nets, and the elements of the nets as he wishes, limiting value of the net being 16 in number, though the maximum value can be as high as 8C2(combination of 2 from the list of 8 vertices)

The nets are provided in a file called nets.txt and is of the form (0,2,4,). This means that the vertices a,c,e whose numerical indices, starting from a as 0  given in the net.txt file, forms one net, and have the same voltage as each other.

How to run the code

Firstly apply the nets with each of the vertices separated by a comma. The last element of each line should also be a ',' so that the code can easly recognize the vertices in between two commas.

Once the nets are correctly entered. Go to terminal and then to the folder in which FM.py is stored.
Eg :

cd /graphml/ffmalgo
where fmalgo contains the codes nets.txt and FM.py

Now type the command for compiling the code:  python   FM.py

This will compile and run the code in the console itslef, and generate the result and tell which partition each of the vertices belong to.
