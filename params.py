from envs import economy
import numpy as np

import tensorflow as tf

vProductivity = np.array([0.9792, ], float)
mTransition = np.array([[1.0, ], float])

alpha = 1.0 / 3.0
delta = 1.0
prod = economy.Production(alpha, delta, vProductivity)
motion = economy.Motion(mTransition)
model = economy.GrowthEconomy(economy.LogUtility(), prod, motion)


def random_nn_parameters(hidden_choices=[[5], [10], [100], [200], [200, 200], [400], [50], [10, 10], [10, 10, 10], [100, 100], [100, 100, 100], [1000]], nonlinearity_choices=[tf.nn.relu, tf.nn.tanh]):
    return {'hidden_layers': np.random.choice(hidden_choices), 'nonlinearity': np.random.choice(nonlinearity_choices)}


def random_learning_parameters(rates=[.01, .001, .002, .0001], discount=[.75, .95, .99], compress=[True, False]):
    return {'learning_rate': np.random.choice(rates), 'discount': np.random.choice(discount), 'compress': np.random.choice(compress)}


def random_strat(lo=[.5, .7, .8, .9], hi=[1.1, 1.2, 1.5, 1.7], max_iters=[40]):
    return {'lo': np.random.choice(lo), 'hi': np.random.choice(hi), 'max_iters': np.random.choice(max_iters)}


def random_parameters():
    nnvParameters = random_nn_parameters()
    nnpchoices = [[], [5], [10], [10], [5, 5], [25], [25, 25]]
    nnpParameters = random_nn_parameters(
        hidden_choices=nnpchoices)
    nnqParameters = random_nn_parameters()
    learningParameters = random_learning_parameters()
    strat = random_strat()
    parameters = {'naf': {
        'nnvParameters': nnvParameters, 'nnpParameters': nnpParameters,
        'nnqParameters': nnqParameters, 'learningParameters': learningParameters}, 'strat': strat}
    return parameters
