# VTruST

This is the code repository for our paper 'VTruST : Controllable value function based subset selection for Data-Centric Trustworthy AI'.

# Getting Started

Run the following commands to setup the environment:

```
git clone https://github.com/SoumiDas/VTruST.git

cd VTruST

conda create --name vtrust --file requirements.txt
```

After the environment gets installed,

```
conda activate vtrust
```

We provide the following instructions for both Fairness and Robustness on COMPAS and CIFAR-10 respectively.

# Current Setup for Fairness

<i>Dataset:</i> COMPAS

<i>Model:</i> 2 layer network

The default parameters are provided in ```config.json```. One can vary the parameters by running ```python config_create.py```

In order to obtain selected datapoints and their scores, from VTruST, run

```python experiment.py```

Train the selected set of datapoints by running

```python compas_subtrain_eval.py```

# Current Setup for Robustness

<i>Dataset:</i> CIFAR-10

<i>Model:</i> ResNet-18

The default parameters are provided in ```config.json```. One can vary the parameters by running ```python config_create.py```

In order to obtain selected datapoints and their scores, from VTruST, run

```python experiment.py```

Train the selected set of datapoints by running

```python train_eval_SA.py```
