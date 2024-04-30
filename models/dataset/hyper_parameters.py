from . import state_space_parameters as ssp
import metaqnn.data_loader as data_loader
import numpy as np

import os

MODEL_NAME = "bench"

# Number of output neurons
NUM_CLASSES = 256  # Number of output neurons

# Input Size
INPUT_SIZE = 2570

# Batch Queue parameters
TRAIN_BATCH_SIZE = 512  # Batch size for training (scaled linearly with number of gpus used)
NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN = 102_400  # Number of training examples
NUM_ITER_PER_EPOCH_TRAIN = NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN / TRAIN_BATCH_SIZE
EVAL_BATCH_SIZE = TRAIN_BATCH_SIZE  # Batch size for validation
NUM_EXAMPLES_PER_EPOCH_FOR_EVAL = 12800 # Number of validation examples

MAX_EPOCHS = 25  # Max number of epochs to train model

# Training Parameters
OPTIMIZER = 'Adam'  # Optimizer (should be in caffe format string)
MAX_LR = 3e-3  # The max LR (scaled linearly with number of gpus used)

# Bulk data folder
BULK_ROOT = 'data/bench/experiment_value/'
DATA_ROOT = BULK_ROOT

print(os.path.abspath(DATA_ROOT + 'bench_key.npy')) #Verifica percorso file
print(os.path.exists(DATA_ROOT + 'bench_key.npy')) #Verifica esistenza file

# Trained model dir
TRAINED_MODEL_DIR = BULK_ROOT + 'trained_models'
DB_FILE = 'models/dataset/bench_dataset/'

VALIDATION_FROM_ATTACK_SET = True

# Unmask files
KEY = np.load(DATA_ROOT + 'bench_key.npy')
ATTACK_KEY_BYTE = 0

ATTACK_PRECOMPUTED_BYTE_VALUES = np.load(DATA_ROOT + f'attack_precomputed_byte{ATTACK_KEY_BYTE}_values.npy')

TRACES_PER_ATTACK = 50 # Maximum number of traces to use per attack
NUM_ATTACKS = 256  # Number of attacks to average the GE over