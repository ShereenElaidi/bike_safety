import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import pandas as pd
import torch.utils.data

# load the data
df = pd.read_csv("converted_data.csv")

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
        self.fc3 = nn.Linear(40, 20)
        self.fc4 = nn.Linear(40, 20)
        self.fc5 = nn.Linear(20, 10)         # Final output: predicing # of possible accidents

    def forward(self, x):
        out = F.relu(self.fc1(x))
        out = F.relu(self.fc2(out))
        out = F.relu(self.fc3(out))
        out = F.relu(self.fc4(out))
        out = self.fc5(out)

        return out



# TODO turn data into numerical: AM - 1, PM - 2, RH - 3; 4 SEASONS: Winter - 1,
# TODO Spring  - 2, Summer - 3, Fall - 4
train_data = torch.utils.data.TensorDataset(torch.from_numpy(x_train).float(),
                                            torch.from_numpy(y_train).long())
val_data = torch.utils.data.TensorDataset(torch.from_numpy(x_val).float(),
                                          torch.from_numpy(y_val).long())
test_data = torch.utils.data.TensorDataset(torch.from_numpy(x_test).float(),
                                           torch.from_numpy(y_test).long())