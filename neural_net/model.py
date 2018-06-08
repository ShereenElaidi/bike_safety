import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import pandas as pd
import torch.utils.data
from random import randint
import pickle

# load the data
df = pd.read_csv("data.csv")

# shuffling the dataframe

df = df.sample(frac=1)

# Generating the training and validation sets
np.random.seed(1234)
train, validate, test = np.split(df.sample(frac=1, random_state=134),
                                 [int(.6*len(df)), int(.8*len(df))])

# We need to drop the count values for the training, validation, and test
x_train = train.drop(['Count'], axis =1).values
y_train = train['Count'].values

x_val = train.drop(['Count'], axis=1).values
y_val = train['Count'].values

x_test = test.drop(['Count'], axis=1).values
y_test = test['Count'].values

# creating the neural net
torch.manual_seed(1234)

class model(nn.Module):
    def __init__(self):
        super(model, self).__init__()
        self.fc1 = nn.Linear(5, 20)
        self.fc2 = nn.Linear(20, 40)
        self.fc3 = nn.Linear(40, 40)
        self.fc4 = nn.Linear(40, 20)
        self.fc5 = nn.Linear(20, 10)         # Final output: predicing # of possible accidents

    def forward(self, x):
        out = F.relu(self.fc1(x))
        out = F.relu(self.fc2(out))
        out = F.relu(self.fc3(out))
        out = F.relu(self.fc4(out))
        out = self.fc5(out)

        return out

print(df.head())

print(df['Count'].max())

# def safe_convert(x, max_val):
#   try:
#     new_x = int(x)
#     return new_x
#   except ValueError:
#     return randint(0, max_val)
#
# max_val_dict = {'Month': 11, 'Day': 30, ...}
#
# new_df = {}
# for key in df.keys():
#   df[key] = [safe_convert(x, max_val_dict[key]) for x in df[key]]
# converting the list from string to int

# for i in range(0, 3741):
#     print(i)
#     df['Year'][i] = int(df["Year"][i])
#     df['Month'][i] = int(df["Month"][i])
#     df['Time'][i] = int(df["Time"][i])
#     try:
#         df['Count'][i] = int(df['Count'][i])
#     except ValueError:
#         df['Count'][i] = randint(0,df['Count'].max())
#     df['Lat'][i] = int(df["Lat"][i])
#     df['Lng'][i] = int(df["Lng"][i])


# Saving the code from above
with open('dictionary.pickle', 'wb') as handle:
    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('dictionary.pickle', 'rb') as handle:
    data = pickle.load(handle)

# pickle.dump(df, 'df.pickle')
# df = pickle.load('df.pickle')


# TODO convert the data to int format: loop through the list of lists, converting each string to int


train_data = torch.utils.data.TensorDataset(torch.from_numpy(x_train).float(),
                                            torch.from_numpy(y_train).long())
val_data = torch.utils.data.TensorDataset(torch.from_numpy(x_val).float(),
                                          torch.from_numpy(y_val).long())
test_data = torch.utils.data.TensorDataset(torch.from_numpy(x_test).float(),
                                           torch.from_numpy(y_test).long())

# defining the model

neural_net = model()
print(model())

# setting the neural net in .eval() mode:

neural_net = neural_net.eval()
data, target = val_data[0:5]
output = neural_net(data)
print(out)
