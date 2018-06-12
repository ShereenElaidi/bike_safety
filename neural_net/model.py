import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import pandas as pd
import torch.utils.data
import pickle
import os

path = os.getcwd()
# load the data
df = pd.read_csv("data.csv")

# pd.DataFrame.hist(df, ['Count'], bins=25)
# plt.show()

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
        self.fc4 = nn.Linear(40, 80)
        self.fc5 = nn.Linear(80, 40)
        self.fc6 = nn.Linear(40, 20)
        self.fc7 = nn.Linear(20, 11)         # Final output: predicing # of possible accidents

    def forward(self, x):
        out = F.relu(self.fc1(x))
        out = F.dropout(out, p=0.5)
        out = F.relu(self.fc2(out))
        out = F.dropout(out, p=0.5)
        out = F.relu(self.fc3(out))
        out = F.dropout(out, p=0.5)
        out = F.relu(self.fc4(out))
        out = F.dropout(out, p=0.5)
        out = F.relu(self.fc5(out))
        out = F.dropout(out, p=0.5)
        out = F.relu(self.fc6(out))
        out = F.dropout(out, p=0.5)
        out = self.fc7(out)
        return out


# UNCOMMENT THIS CODE WHENEVER YOU CHANGE THE DATA
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

train_data = torch.utils.data.TensorDataset(torch.from_numpy(x_train).float(),
                                            torch.from_numpy(y_train).long())
val_data = torch.utils.data.TensorDataset(torch.from_numpy(x_val).float(),
                                          torch.from_numpy(y_val).long())
test_data = torch.utils.data.TensorDataset(torch.from_numpy(x_test).float(),
                                           torch.from_numpy(y_test).long())

# defining the model
neural_net = model()

# setting the neural net in .eval() mode:
neural_net = neural_net.eval()
data, target = val_data[0:1]
output = neural_net(data)
output_prob = F.softmax(output,dim=1)

# loss function
def cost_function(prediction, target):
    loss = F.cross_entropy(prediction, target)
    return loss

# optimizer
optimizer = optim.Adam(neural_net.parameters(), lr=0.0001)
train_batch_size = 32
eval_batch_size = 32
train_loader = torch.utils.data.DataLoader(train_data, batch_size = train_batch_size, shuffle =True)
val_loader = torch.utils.data.DataLoader(val_data, batch_size = eval_batch_size, shuffle = False)
test_loader = torch.utils.data.DataLoader(test_data, batch_size = eval_batch_size, shuffle=False)

# training function
def train(epoch, model, train_loader, optimizer):
    # setting the model in .train() mode
    model.train()
    total_loss = 0
    correct=0

    # to save the best model regardless of when in the training it occured
    acc_optimal = 0
    loss_train = np.empty([numEpochs])
    loss_valid = np.empty([numEpochs])
    acc_train = np.empty([numEpochs])
    acc_valid = np.empty([numEpochs])

    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        prediction = model(data)
        loss = cost_function(prediction, target)
        loss.backward()
        optimizer.step()
        total_loss += loss.data.item()*len(data)
        pred_classes = prediction.data.max(1,keepdim=True)[1]
        correct += pred_classes.eq(target.data.view_as(pred_classes)).sum().double()

        # saving the best model
        model.eval()
        loss_train[epoch-1], acc_train[epoch-1] = eval(model, train_loader)
        loss_valid[epoch-1], acc_valid[epoch-1] = eval(model, val_loader)
        if (acc_valid[epoch-1] >acc_optimal):
            acc_optimal = acc_valid[epoch-1]
            epoch_optimal = epoch
            torch.save(model.state_dict(), path+'/Model_optimal.pth')

    # compute mean loss
    mean_loss = total_loss/len(train_loader.dataset)
    acc = correct/len(train_loader.dataset)
    print('Train Epoch: {}   Avg_Loss: {:.5f}   Acc: {}/{} ({:.3f}%)'.format(
        epoch, mean_loss, correct, len(train_loader.dataset),
        100. * acc))
    return mean_loss, acc

# evaluation function
def eval(model, eval_loader):
    model.eval()
    total_loss = 0
    correct = 0

    for batch_fix, (data, target) in enumerate(eval_loader):
        prediction = model(data)
        loss = cost_function(prediction, target)
        total_loss += loss.data[0]*len(data)
        pred_classes = prediction.data.max(1,keepdim=True)[1]
        correct += pred_classes.eq(target.data.view_as(pred_classes)).sum().double()

    # compute mean loss
    mean_loss = total_loss/len(eval_loader.dataset)
    acc = correct/len(eval_loader.dataset)
    print('Eval:  Avg_Loss: {:.5f}   Acc: {}/{} ({:.3f}%)'.format(
        mean_loss, correct, len(eval_loader.dataset),
        100. * acc))
    return mean_loss, acc

# save the model
def save_model(epoch, model, path='./'):
    filename = path+'neural_network_{}.pt'.format(epoch)
    torch.save(model.state_dict(), filename)
    return model

# load the model
def load_model(epoch, model, path='./'):
    filename = path + 'neural_network_{].pt'.format(epoch)
    model.load_state_dict(torch.load(filename))
    return model

numEpochs = 50
checkpoint_freq = 10
path='./'
train_losses = []
val_losses = []
train_accuracies = []
val_accuracies = []

for epoch in range(1, numEpochs+1):
    train_loss, train_acc = train(epoch, neural_net, train_loader, optimizer)
    val_loss, val_acc = eval(neural_net, val_loader)
    train_losses.append(train_loss)
    val_losses.append(val_loss)
    train_accuracies.append(train_acc)
    val_accuracies.append(val_acc)
    if epoch % checkpoint_freq == 0:
        save_model(epoch, neural_net, path)

# Saving the model
save_model(numEpochs, neural_net, path)
print("\n\n\nOptimization ended. Done!\n")

# testing the trained model out
neural_net = neural_net.eval()
data, target = val_data[0:5]
output = neural_net(data)
test_loss, test_acc = eval(neural_net, test_loader)

# Plotting the learning curve
x = list(range(len(train_losses)))
ax = plt.subplot(111)
plt.plot(x, train_losses, 'r', label="Train")
plt.plot(x, val_losses, 'g', label="Validation")
plt.title('Loss')
leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.99)
plt.show()

# Plotting the accuracy curve
x = list(range(len(train_accuracies)))
ax = plt.subplot(111)
plt.plot(x, train_accuracies, 'r', label="Train")
plt.plot(x, val_accuracies, 'g', label="Validation")
plt.title('Accuracy')
leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=False, fancybox=False)
leg.get_frame().set_alpha(0.99)
plt.show()
exit()