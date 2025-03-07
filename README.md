# chess-heatmap
A python project which generates control heatmap images for given chess games in parallel using dask running on a coiled cluster.

### Background
Dask provides a framework for distributed computing in Python which helps scale-up our computations. Dask Collections create task graphs that define how to perform the computation in parallel. Coiled is a deployment-as-a-service library that makes it easy to scale dask on Cloud. It provides hosted dask clusters where the actual computation is performed.

### About this project
Heatmap visualization shows how much control each color has on a square for each ply in the chess board. It can be used to analyze important squares, observe how the control pattern changes, create a strategy or pick good plans.
Chess games need to be provided as input in form of PGN files. An animated GIF is generated per game which captures the heatmap, with each ply as a frame in the GIF. Dask futures have been used to handle multiple games in parallel. Power of each square in a ply for each game is again computed in parallel. Each of these dask tasks are run on a Coiled cluster.

### Setup

1. Clone the repository

2. Setup and activate a virtual environment: <br />
    `virtualenv env` <br />
    `env\Scripts\activate` <br />
    
3. Run the command to install all packages:<br />
    `pip install -r requirements.txt`
    
4. Create an account with Coiled - https://coiled.io/ (At the time of this writing, Coiled is in Beta version)

5. Activate coiled in local environment (instructions present in https://docs.coiled.io/user_guide/getting_started.html) <br />
    `coiled login --token <token>`
    
6. The chess games that need to be visualized should be given in a PGN file (or multiple files). These files should be placed in **resources/input** folder. 

7. (Optional) Open **config/config.yaml** and modify the parameters (like number of workers, worker cpu, etc) that suit your needs. <br />
Note: This module can also be run on a Local cluster (your laptop). To do that, uncomment the 'LocalConfig' section. 

### Run the project
- To generate heatmaps, run the chess_heatmap file <br />
`python chess_heatmap.py` <br />

- Check the **resources/output** folder to see the generated gif. 

### Example
A chess game of Donald Byrne vs. Robert James Fischer, 1956 has been included as an example. 

![0 Third Rosenwald Trophy](https://user-images.githubusercontent.com/62924721/113397389-90f35b80-93ba-11eb-85ae-b1ac11e57cc9.gif)

### How to read the heatmap
- Each game will have a corresponding heatmap. If a PGN has 5 games, there will be 5 gif files with event name (preceeded by number) as the file name.
- Each gif consists of heatmaps for White and Black respectively.
- Each frame in a gif is the heatmap for a ply in that game. All the heatmaps(for each ply) in a game combined together form the animated gif.
- The legend represents the number of attackers (for each square).

Here is an example of a single ply and its heatmap

![Single_ply](https://user-images.githubusercontent.com/62924721/110592466-5114cc00-81a0-11eb-9329-e241feb6531e.jpg) ![0 Single Ply](https://user-images.githubusercontent.com/62924721/113398033-9604da80-93bb-11eb-88bd-af6a26cb8048.gif)

In the heatmap gif, the first frame represents for each square, how many pieces of White have control (on that particular square). For instance, consider square f3. If White had a piece on f3, how many defenders does it have when it is captured. It is like a series of consecutive captures happening on f3 and the Queen on d1 will play a role. So, the control for that square will be 4. <br/>
Similarly, the second frame represents for each square how many pieces of Black have control. 

Using this we can see how the control pattern changes when certain moves are created and it is also a good way to visualize some of the deeper positional moves.

