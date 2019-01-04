import numpy as np
import matplotlib.pyplot as plt

import torch.nn as nn


def inputs_reshape(array, Lin):

    Nb, Lseq = array.shape
    array_reshaped = np.empty([Lseq-Lin+1, Nb, Lin])

    for n in range(Lseq-Lin+1):
        array_reshaped[n, :, :] = array[:, n:n+Lin]

    return array_reshaped



class RNN_for_Ringdown(nn.Module):

    def __init__(self, Lin):
        super(RNN_for_Ringdown, self).__init__()
        self.rnn = nn.RNN()
