import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import pandas as pd
import torch.utils.data

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


print(train['Lat'])
print(df.head())

# TODO convert the data to int format: loop through the list of lists, converting each string to int
# TODO convert  AM, PM, RH to 1,2,3. NaN ==> randomly
# TODO convert remove NaN's from the count dataset

# train_data = torch.utils.data.TensorDataset(torch.from_numpy(x_train).float(),
#                                             torch.from_numpy(y_train).long())
# val_data = torch.utils.data.TensorDataset(torch.from_numpy(x_val).float(),
#                                           torch.from_numpy(y_val).long())
# test_data = torch.utils.data.TensorDataset(torch.from_numpy(x_test).float(),
#                                            torch.from_numpy(y_test).long())