import torch
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader, Subset
from sklearn.model_selection import KFold
import pandas as pd
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

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

# Define the CNN architecture
class NeuralNetSimple(nn.Module):
    """
    A simple fully connected neural network.
    """
    def __init__(self):
        super(NeuralNetSimple, self).__init__()
        self.fcLayer1 = nn.Linear(784, 128)
        self.fcLayer2 = nn.Linear(128, 10)

    def forward(self, inputData):
        """
        Forward pass of the network.
        """
        inputData = torch.flatten(inputData, 1)
        inputData = self.fcLayer1(inputData)
        inputData = nn.functional.relu(inputData)
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
    totalLoss = 0
    for batchIndex, (data, target) in enumerate(dataLoader):
        data, target = data.to(computingDevice), target.to(computingDevice)
        optimizerInstance.zero_grad()
        output = neuralNet(data)
        loss = nn.functional.nll_loss(output, target)
        loss.backward()
        optimizerInstance.step()
        totalLoss += loss.item()
    averageLoss = totalLoss / len(dataLoader)
    return averageLoss

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
    return testLoss, accuracy

# Define the data transformations
dataTransformations = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# Load the dataset
datasetInstance = CSVDataLoader('MNIST.csv', transform=dataTransformations)

# Initialize the KFold class
kfoldInstance = KFold(n_splits=5, shuffle=True)
accuracyListCNN = []
accuracyListNN = []

# Initialize the lists for storing train/test losses and accuracies for each epoch
trainLossesCNN = []
testLossesCNN = []
testAccuraciesCNN = []
trainLossesNN = []
testLossesNN = []
testAccuraciesNN = []

# Perform k-fold cross-validation
for foldIndex, (trainIndices, testIndices) in enumerate(kfoldInstance.split(datasetInstance)):
    
    # Clear the lists for the new fold
    trainLossesCNN.clear()
    testLossesCNN.clear()
    testAccuraciesCNN.clear()
    trainLossesNN.clear()
    testLossesNN.clear()
    testAccuraciesNN.clear()
    
    print(f'FOLD {foldIndex+1}')
    print('--------------------------------')

    trainSubset = Subset(datasetInstance, trainIndices)
    testSubset = Subset(datasetInstance, testIndices)

    trainDataLoader = DataLoader(trainSubset, batch_size=64, shuffle=True)
    testDataLoader = DataLoader(testSubset, batch_size=64, shuffle=False)

    computingDevice = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Train and test the CNN
    neuralNetInstance = NeuralNet().to(computingDevice)
    optimizerInstance = optim.SGD(neuralNetInstance.parameters(), lr=0.01, momentum=0.5)
    for epochNumber in range(1, 5):
        trainLossCNN = trainModel(neuralNetInstance, computingDevice, trainDataLoader, optimizerInstance, epochNumber)
        testLossCNN, accuracyCNN = testModel(neuralNetInstance, computingDevice, testDataLoader)
        trainLossesCNN.append(trainLossCNN)
        testLossesCNN.append(testLossCNN)
        testAccuraciesCNN.append(accuracyCNN)

    # Train and test the NN
    neuralNetInstance = NeuralNetSimple().to(computingDevice)
    optimizerInstance = optim.SGD(neuralNetInstance.parameters(), lr=0.01, momentum=0.5)
    for epochNumber in range(1, 5):
        trainLossNN = trainModel(neuralNetInstance, computingDevice, trainDataLoader, optimizerInstance, epochNumber)
        testLossNN, accuracyNN = testModel(neuralNetInstance, computingDevice, testDataLoader)
        trainLossesNN.append(trainLossNN)
        testLossesNN.append(testLossNN)
        testAccuraciesNN.append(accuracyNN)

    # For CNN
    print(f'Accuracy for fold {foldIndex+1} (CNN): {testAccuraciesCNN[-1]*100:.2f}%')  # Print the accuracy for this fold
    accuracyListCNN.append(testAccuraciesCNN[-1])

    # For NN
    print(f'Accuracy for fold {foldIndex+1} (NN): {testAccuraciesNN[-1]*100:.2f}%')  # Print the accuracy for this fold
    accuracyListNN.append(testAccuraciesNN[-1])

    # Plot the learning curve
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, 5), trainLossesCNN, label='Train CNN')
    plt.plot(range(1, 5), testLossesCNN, label='Test CNN')
    plt.plot(range(1, 5), trainLossesNN, label='Train NN')
    plt.plot(range(1, 5), testLossesNN, label='Test NN')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(range(1, 5), testAccuraciesCNN, label='CNN')
    plt.plot(range(1, 5), testAccuraciesNN, label='NN')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.tight_layout()
    plt.savefig('learning_curve.png')  # Save the plot as a PNG file
    plt.show()

# Calculate and print the average accuracy
averageAccuracyCNN = sum(accuracyListCNN) / len(accuracyListCNN)
averageAccuracyNN = sum(accuracyListNN) / len(accuracyListNN)
print('Average accuracy CNN: {:.2f}%'.format(averageAccuracyCNN * 100))
print('Average accuracy NN: {:.2f}%'.format(averageAccuracyNN * 100))