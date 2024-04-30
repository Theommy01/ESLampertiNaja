Reinforcement Learning for Profiled Side-Channel Analysis
========
This is a project done for the course Embedded Systems in Politecnico di Milano.
The goal was to take the project that can be found at the folder https://github.com/dade145/Reinforcement-Learning-for-SCA and update it to support Keras 3.0 and Python 3.11.
To do so we used Ubuntu 22.0.4, since is the only OS that do not cause problems with packages.
The code for the experiments generating SCA CNNs can be found in the `metaqnn` folder.
The model used is inside the `dataset` folder.
To run an experiment, use `python -m metaqnn.main dataset`.

requirements.txt includes all requirements including the exact dependencies used.

To generate the files "bench_key.npy" and "attack_precomputed_byto0" just run Helper.py.

Inside the folder "data/bench/experiment_value/trained_models" can be found models that are already trained on the dataset we had, while in "data/bench/experiment_value/graphs" there are the plots of the results.

#
Here are some examples of plots obtained after running the code:

![Running helper](https://github.com/Theommy01/ESLampertiNaja/blob/main/images/running_helper.png)

![Network building - 1](https://github.com/Theommy01/ESLampertiNaja/blob/main/images/Running%20main%201.png)

![Network building - 2](https://github.com/Theommy01/ESLampertiNaja/blob/main/images/Running%20main%202.png)

![Epoch execution](https://github.com/Theommy01/ESLampertiNaja/blob/main/images/Epoch.png)

![Bench_0001 Graph](https://github.com/Theommy01/ESLampertiNaja/blob/main/images/Graph.png)

#
**This code is partially based on:**

**[Designing Neural Network Architectures Using Reinforcement Learning](https://arxiv.org/pdf/1611.02167.pdf)**   
Bowen Baker, Otkrist Gupta, Nikhil Naik, Ramesh Raskar  
*International Conference on Learning Representations*, 2017

The source code of which can be found on [Github](https://github.com/bowenbaker/metaqnn/) under the MIT License.
