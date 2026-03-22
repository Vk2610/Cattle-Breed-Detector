from torchvision import transforms
from PIL import Image

transform = transforms.Compose([
    transforms.Lambda(lambda image: image.convert('RGB')),
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])