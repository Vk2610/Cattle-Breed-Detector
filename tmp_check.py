# !/usr/bin/env python
# Description : This script loads a PyTorch model from a specified path, extracts the shapes of the parameters related to the classifier, and saves this information in a JSON file.

import torch, json
sd = torch.load('model/model.pth', map_location='cpu')
res = {}
for k in sd:
    if 'classifier' in k:
        res[k] = list(sd[k].shape)
with open('out.json', 'w') as f:
    json.dump(res, f, indent=2)
