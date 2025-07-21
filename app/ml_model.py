import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from app.config import Config

model = models.resnet34(weights=None)

num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, len(Config.CLASSES))

model.load_state_dict(torch.load(Config.MODEL_PATH, map_location='cpu'))
model.eval()

transform = transforms.Compose([
    transforms.Resize(224),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


def predict(image_path):
    img = Image.open(image_path).convert('RGB')
    img = transform(img).unsqueeze(0)
    with torch.inference_mode():
        outputs = model(img)
        probs = torch.nn.functional.softmax(outputs, dim=1)
        pred_idx = torch.argmax(probs).item()
        confidence = probs[0][pred_idx].item()
    return Config.CLASSES[pred_idx], confidence
