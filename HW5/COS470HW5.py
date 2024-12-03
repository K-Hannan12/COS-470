from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np

# Kaleb Hannan
# HW5
# 11/25/24

# Get test data
data = pd.read_csv('HW5/homework5_data.csv')

# Get input data
BBData = data.iloc[:, 1:-2]

# Get label (Games Won)
gamesWon = data.iloc[:,0]

# Norlize data between 0 - 1
normilizedBBData = (BBData - BBData.min()) / (BBData.max() - BBData.min())


# Split data randomly 15% test 85% traning
traning_data,test_data, traning_label, test_label = train_test_split(normilizedBBData, gamesWon,train_size=0.85, test_size= 0.15, random_state=42)


# Change data type to tensors
traning_data = torch.tensor(traning_data.values, dtype=torch.float32)
traning_label = torch.tensor(traning_label.values, dtype=torch.float32).view(-1,1)
test_data = torch.tensor(test_data.values, dtype=torch.float32)
test_label = torch.tensor(test_label.values, dtype=torch.float32).view(-1,1)


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

epochs = 10000
learning_Rate = 0.0001

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=learning_Rate)


# Train model
for epoch in range(epochs):
    # Get perdiction
    y_pred = model(traning_data)
    # Compute loss
    loss = criterion(y_pred, traning_label)

    
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
for i in range(10):
    print(f"True value: {test_label[i].item():.2f}, Predicted value: {perdiction[i].item():.2f}")