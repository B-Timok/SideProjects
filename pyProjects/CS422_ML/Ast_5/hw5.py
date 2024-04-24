import torch
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader, Subset
from sklearn.model_selection import KFold
import pandas as pd
import torchvision.transforms as transforms

# Define the neural network architecture
class NeuralNet(nn.Module):
    """
    A simple convolutional neural network.
    """
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.convLayer1 = nn.Conv2d(1, 32, 3, 1)
        self.convLayer2 = nn.Conv2d(32, 64, 3, 1)
        self.dropoutLayer1 = nn.Dropout(0.25)
        self.dropoutLayer2 = nn.Dropout(0.5)
        self.fcLayer1 = nn.Linear(9216, 128)
        self.fcLayer2 = nn.Linear(128, 10)

    def forward(self, inputData):
        """
        Forward pass of the network.
        """
        inputData = self.convLayer1(inputData)
        inputData = nn.functional.relu(inputData)
        inputData = self.convLayer2(inputData)
        inputData = nn.functional.relu(inputData)
        inputData = nn.functional.max_pool2d(inputData, 2)
        inputData = self.dropoutLayer1(inputData)
        inputData = torch.flatten(inputData, 1)
        inputData = self.fcLayer1(inputData)
        inputData = nn.functional.relu(inputData)
        inputData = self.dropoutLayer2(inputData)
        inputData = self.fcLayer2(inputData)
        outputData = nn.functional.log_softmax(inputData, dim=1)
        return outputData

class CSVDataLoader(Dataset):
    """
    A custom Dataset class for loading data from a CSV file.
    """
    def __init__(self, filePath, transform=None):
        self.dataFrame = pd.read_csv(filePath)
        self.transform = transform

    def __len__(self):
        return len(self.dataFrame)

    def __getitem__(self, index):
        """
        Returns a tuple (image, label) for the given index.
        """
        image = self.dataFrame.iloc[index, 1:].values.astype('uint8').reshape((28, 28, 1))
        label = self.dataFrame.iloc[index, 0]
        
        if self.transform is not None:
            image = self.transform(image)
            
        return image, label

def trainModel(neuralNet, computingDevice, dataLoader, optimizerInstance, epochNumber):
    """
    Trains the model for one epoch.
    """
    neuralNet.train()
    for batchIndex, (data, target) in enumerate(dataLoader):
        data, target = data.to(computingDevice), target.to(computingDevice)
        optimizerInstance.zero_grad()
        output = neuralNet(data)
        loss = nn.functional.nll_loss(output, target)
        loss.backward()
        optimizerInstance.step()
        if batchIndex % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epochNumber, batchIndex * len(data), len(dataLoader.dataset),
                100. * batchIndex / len(dataLoader), loss.item()))

def testModel(neuralNet, computingDevice, dataLoader):
    """
    Tests the model on the test set.
    """
    neuralNet.eval()
    testLoss = 0
    correctPredictions = 0
    with torch.no_grad():
        for data, target in dataLoader:
            data, target = data.to(computingDevice), target.to(computingDevice)
            output = neuralNet(data)
            testLoss += nn.functional.nll_loss(output, target, reduction='sum').item()
            pred = output.argmax(dim=1, keepdim=True)
            correctPredictions += pred.eq(target.view_as(pred)).sum().item()

    testLoss /= len(dataLoader.dataset)
    accuracy = correctPredictions / len(dataLoader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        testLoss, correctPredictions, len(dataLoader.dataset),
        100. * accuracy))

    return accuracy

# Define the data transformations
dataTransformations = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# Load the dataset
datasetInstance = CSVDataLoader('MNIST.csv', transform=dataTransformations)

# Initialize the KFold class
kfoldInstance = KFold(n_splits=5, shuffle=True)
accuracyList = []

# Perform k-fold cross-validation
for foldIndex, (trainIndices, testIndices) in enumerate(kfoldInstance.split(datasetInstance)):
    print(f'FOLD {foldIndex}')
    print('--------------------------------')

    trainSubset = Subset(datasetInstance, trainIndices)
    testSubset = Subset(datasetInstance, testIndices)

    trainDataLoader = DataLoader(trainSubset, batch_size=64, shuffle=True)
    testDataLoader = DataLoader(testSubset, batch_size=64, shuffle=False)

    computingDevice = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    neuralNetInstance = NeuralNet().to(computingDevice)
    optimizerInstance = optim.SGD(neuralNetInstance.parameters(), lr=0.01, momentum=0.5)

    # Train and test the model
    for epochNumber in range(1, 5):
        trainModel(neuralNetInstance, computingDevice, trainDataLoader, optimizerInstance, epochNumber)
    
    accuracy = testModel(neuralNetInstance, computingDevice, testDataLoader)
    accuracyList.append(accuracy)

# Calculate and print the average accuracy
averageAccuracy = sum(accuracyList) / len(accuracyList)
print('Average accuracy: {:.2f}%'.format(averageAccuracy * 100))