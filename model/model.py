# Description : This file defines a PyTorch model for cattle breed classification.
import torch.nn as nn
from torchvision.models import efficientnet_v2_s

class CattleModel(nn.Module):
    def __init__(self, num_classes=50):
        super(CattleModel, self).__init__()
        
        # The weights were trained on EfficientNetV2-S
        self.backbone = efficientnet_v2_s(weights=None)
        
        # Reconstruct the custom classifier matching the saved weights exactly
        self.backbone.classifier = nn.Sequential(
            nn.Dropout(p=0.2, inplace=False),  # 0
            nn.Linear(1280, 512, bias=True),   # 1
            nn.BatchNorm1d(512),               # 2
            nn.ReLU(),                         # 3
            nn.Dropout(p=0.2, inplace=False),  # 4
            nn.Linear(512, 256, bias=True),    # 5
            nn.BatchNorm1d(256),               # 6
            nn.ReLU(),                         # 7
            nn.Dropout(p=0.2, inplace=False),  # 8
            nn.Linear(256, num_classes, bias=True) # 9
        )

    def forward(self, x):
        return self.backbone(x)