import numpy as np

root = "models/dataset/bench_dataset/"
test_meta = np.load(root+"test_meta.npy", mmap_mode='r')
test_targets = np.load(root+"test_targets.npy", mmap_mode='r')
test_windows = np.load(root+"test_windows.npy", mmap_mode='r')

train_meta = np.load(root+"train_meta.npy", mmap_mode='r')
train_targets = np.load(root+"train_targets.npy", mmap_mode='r')
train_windows = np.load(root+"train_windows.npy", mmap_mode='r')

valid_meta = np.load(root+"valid_meta.npy", mmap_mode='r')
valid_targets = np.load(root+"valid_targets.npy", mmap_mode='r')
valid_windows = np.load(root+"valid_windows.npy", mmap_mode='r')

print(test_meta.shape)
print(test_targets.shape)
print(test_windows.shape)
print('\n')
print(train_meta.shape)
print(train_targets.shape)
print(train_windows.shape)
print('\n')
print(valid_meta.shape)
print(valid_targets.shape)
print(valid_windows.shape)

DIM_TEST = 12800

print(test_meta[0])  #(primo byte plaintext, primo byte key) -- key cambia ogni 102
print(test_meta[100])
print(test_meta[200])
#print(train_windows.dtype)

# Importing the library
import psutil

# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])

profiling_traces = np.concatenate((train_windows, valid_windows))
profiling_targets = np.concatenate((train_targets, valid_targets))

print('RAM memory % used:', psutil.virtual_memory()[2])

key = []
for i in range(DIM_TEST):
    key.append(test_meta[i][1])

np.save("bench_key.npy", key)

from metaqnn.attack.utils import generate_precomputed_values_file

plaintexts = []

for i in range(DIM_TEST):
    plaintexts.append(test_meta[i][0])

generate_precomputed_values_file(plaintext=np.array(plaintexts), byte=0, save_folder="data/bench/experiment_value/")
