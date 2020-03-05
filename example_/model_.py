import string
import torch
import torch.nn as nn
import numpy as np
from example.settings import MODEL_ROOT


all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)

def letterToIndex(letter):
    return all_letters.find(letter)

# Just for demonstration, turn a letter into a <1 x n_letters> Tensor
def letterToTensor(letter):
    tensor = torch.zeros(1, n_letters)
    tensor[0][letterToIndex(letter)] = 1
    return tensor

# Turn a line into a <line_length x 1 x n_letters>,
# or an array of one-hot letter vectors
def lineToTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letterToIndex(letter)] = 1
    return tensor

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()

        self.hidden_size = hidden_size

        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        if torch.cuda.is_available():
          input, hidden = input.cuda(), hidden.cuda()
        combined = torch.cat((input, hidden), 1)
        hidden = nn.LeakyReLU()(self.i2h(combined))
        output = nn.LeakyReLU()(self.i2o(combined))
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)

loaded = torch.load(MODEL_ROOT+"/rnn_url.pt",map_location=torch.device('cpu'))

rnn = RNN(n_letters,20,3)
rnn.load_state_dict(loaded['state_dict'])
rnn.eval()

all_categories = ['url','link','normal']

def predict(line):
    lineTensor = lineToTensor(line)
    hidden = rnn.initHidden()
    for i in range(lineTensor.size()[0]):
        output,hidden = rnn(lineTensor[i],hidden)

    return all_categories[output.max(-1)[-1][0]]
