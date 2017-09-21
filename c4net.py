import numpy as np


class general_net:

    def __init__(self, input_layer,layer_sizes):
        np.vectorize(self.ReLU)
        np.vectorize(self.softmax)
        self.layers = [input_layer]
        self.synapses = []
        final_layer_flag = False
        for i in range(0, len(layer_sizes)):
            syn = 2 * (np.random.random(((layer_sizes[i - 1]),layer_sizes[i]))) - 1
            self.synapses.append(syn)
            if i == len(layer_sizes) - 1:
                final_layer_flag = True
            self.layers.append(self.advance_layer(self.layers[i], self.synapses[i], final_layer_flag))

        #self.layers.append(self.advance_layer(self.layers[-1],self.synapses[-1],final_layer = True))

    # layer: a list of values representing the current layer
    # next_layer_size: the desired number of nodes in the output layer
    # synapses: [number of nodes in current layer X number of nodes in output] matrix of weights
    def advance_layer(self, input_layer, synapses, final_layer = False):
        input_node_count = len(input_layer)
        output_node_count = len(synapses[0])
        output_layer = np.zeros([output_node_count])
        for i in range(0, output_node_count):
            for j in range(0, input_node_count):
                output_layer[i] += input_layer[j] * synapses[j][i]

        if final_layer == True:
            return (self.softmax(output_layer))
        return self.ReLU(output_layer)

    def ReLU(self, x):                  #  MUST BE VECTORIZED WITH np.vectorize(ReLU)  #
        return ((x > 0) * x)

    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

