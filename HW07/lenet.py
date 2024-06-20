# https://github.com/ccc112b/py2cs/tree/master/03-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/05-%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF/02-%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92/01-MNIST
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 50, kernel_size=5)
        self.conv2 = nn.Conv2d(50, 10, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(160, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2(x), 2))
        x = x.view(-1, 160)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return x