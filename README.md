# GridRobotIA
 
# 👥 Developers

| Profile Picture | Developer |
|---------------|------------|
| <img src="https://github.com/wavering-ruby.png" width="100"> | **[Mateus G. M. de Paula](https://github.com/wavering-ruby)** |
| <img src="https://github.com/caiovj18.png" width="100"> | **[Caio Viana de Jesus](https://github.com/caiovj18)** |

# Project's Objetive

The chosen theme to the realization of this project it's Navigation of a Robot, consisting guiding a robot inside a warehouse to carry packeges from origin (A) to the destiny (B), using the minitum time possible, seeing routes and deviating from collision.

## 1. Environment Modeling

The environment of the movimentation of the robot it's represented by a graph or a grid. Each cell of the grid or node of a graph represents one position of the space.

The obstacles is marked as inacessible cells or nodes.

You will see, that some algorithms are used in weight cases or non weight cases of a graph.

## 2. Definition of the Origin and Destiny

The robot starts on a initial point (initial node or cell) and needs to find a route to the objective point (final node or cell).

## 3. Technologies
<div align="center">

![Python](https://img.shields.io/badge/Python_3.13.2-3776AB?style=for-the-badge&logo=python&logoColor=FFFFFF)

</div>

For this project Python it's the only utilized language. The user interface was create using the libraries `Pygame` and `Pygame_gui`, because are more simple for the developers to organize the screen of the project.

This project also uses matrix for the grid and graph algorithms, so `numpy` it's installed to generate a grid with `0` and `random` for the position of the cell colision (with the value of nine). In the future, will be used `time` for timing resolution of the graph, and others modifications.

## 4. Running the Project

### 4.1. Required Libraries:
To run the program, you need to install some libraries before debugging the file. These include:
- Pygame (`pip install pygame`)
- Pygame_gui (`pip install pygame_gui`)
- Numpy (`pip install numpy`)
- Random (`pip install random`)

### 4.2. File Initialization
To execute the program, you need to debug the file **"Interface.py"**, which contains the programming for the sidebar menu. Upon opening it, you will see options to select the desired algorithm (Breadth-First Search, Depth-First Search, Limited Depth Search, Iterative Deepening, or Bidirectional Search).

Next, you must specify:
- The robot's starting position (coordinates X, Y).
- The final position (coordinates X, Y).

After setting these parameters, simply click **"Start"** for the robot's animation to begin.  
If you want to generate a new random grid, click the **"Reset Grid"** button. This will also reset the animation.

For the **Limited Depth Search** algorithm, the depth limit is set to **99** by default. If you need to modify it, change the function call in `find_path`:  
`self.find_path_profundidade_limitada(limite=X)`, where **X** represents the desired depth limit.  
If the solution path exceeds the limit, the robot will not move.

**Note:** If you set the "starting position" or "final position" as an obstacle, it will become a viable path.

### 4.3. Step-by-Step Guide:
1. Debug the **"Interface.py"** file (via terminal or a compiler, as desired).
   - If using a terminal, type: `python interface.py`
2. Click the **"Reset Grid"** button if you want to generate a new random field.
3. In the algorithm selection box, click the name of the algorithm you want to visualize.
4. In the **"Initial Position"** field, enter the coordinates of the point where the robot should start, using the format: `(X, Y)`.
5. In the **"Final Position"** field, enter the coordinates of the point where the robot should end, using the format: `(X, Y)`.
6. For limited algorithm, you can also input the limit cost to run the script.
7. Click the **"Start"** button to execute the robot's animation path.
