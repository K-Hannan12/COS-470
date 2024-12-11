import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import matplotlib.pyplot as plt

# Kaleb Hannan
# HW5
# 11/25/24

# Get test data
traning_data = pd.read_csv('HW5/traning_data_percent.csv')
test_data = pd.read_csv('HW5/test_data_percent.csv')

# Get input data
traning_BBData = traning_data.iloc[:, 1:-2]
test_BBData = test_data.iloc[:, 1:-2]

# Get label (Games Won)
traning_gamesWon = traning_data.iloc[:,0]
test_gamesWon = test_data.iloc[:,0]

# Norlize data between 0 - 1
traningNormilizedBBData = (traning_BBData - traning_BBData.min()) / (traning_BBData.max() - traning_BBData.min())
testNormilizedBBData = (test_BBData - traning_BBData.min()) / (traning_BBData.max() - traning_BBData.min())


# Change data type to tensors
traning_data = torch.tensor(traningNormilizedBBData.values, dtype=torch.float32)
traning_label = torch.tensor(traning_gamesWon.values, dtype=torch.float32).view(-1,1)
test_data = torch.tensor(testNormilizedBBData.values, dtype=torch.float32)
test_label = torch.tensor(test_gamesWon.values, dtype=torch.float32).view(-1,1)


class BBModel(nn.Module):
    def __init__(self,input_size):
        super().__init__()
        self.linear_relu_stack = nn.Sequential(
        nn.Linear(input_size, 64),
        nn.ReLU(),
        nn.Linear(64,32),
        nn.ReLU(),
        nn.Linear(32,16),
        nn.ReLU(),
        nn.Linear(16,1)
        )
    def forward(self, x):
        x = self.linear_relu_stack(x)
        return x


input_size = traning_data.shape[1]
model = BBModel(input_size)

epochs = 1000
learning_Rate = 0.001

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), learning_Rate)

# Array for storing loss values
lossArray = []

# Train model
for epoch in range(epochs):

    # Get perdiction
    y_pred = model(traning_data)
    
    # Compute loss
    loss = criterion(y_pred, traning_label)

    # add loss to array
    lossArray.append(loss.item())
    
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

    # Print the loss at intervals to monitor training
    if (epoch+1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")


model.eval()

with torch.no_grad():
    perdiction = model(test_data)

test_loss = criterion(perdiction,test_label)

print(f"Test Loss: {test_loss.item():.4f}\n")
for i in range(10):  # Print the first 10 examples
    print(f"True value: {test_label[i].item():.2f}, Predicted value: {perdiction[i].item():.2f}")

# Create loss plot
plt.plot(lossArray, label = "Loss")
plt.xlabel('epoch')
plt.ylabel('total loss')
plt.xlim(0, len(lossArray))
plt.ylim(0, max(lossArray) + 0.1)
plt.grid(True)
plt.show()