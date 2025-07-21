import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models
from torchvision.models.resnet import ResNet34_Weights
from prepare_data import train_loader, test_loader, num_classes
from utils.smart_sleep import smart_sleep, get_cpu_temp

model = models.resnet34(weights=ResNet34_Weights.IMAGENET1K_V1)

num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, num_classes)

device = torch.device('cpu')
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
num_epochs = 20

for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        smart_sleep()
        running_loss += loss.item()
    print(f'Epoch {epoch + 1}, Loss: {running_loss / len(train_loader)}')
    print(f'Current CPU temperature: {get_cpu_temp()}°C')

model.eval()
correct = 0
total = 0
with torch.inference_mode():
    for inputs, labels in test_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
print(f'Accuracy on test set: {100 * correct / total}%')

torch.save(model.state_dict(), '../models/leaf_disease_model.pth')
print('Model trained and saved!')
