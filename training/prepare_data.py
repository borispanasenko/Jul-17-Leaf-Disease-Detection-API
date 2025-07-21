from sklearn.model_selection import train_test_split
from torchvision import transforms, datasets
from torch.utils.data import DataLoader, Subset
from sklearn.preprocessing import LabelEncoder
import random

DATASET_PATH = '../data/PlantDisease/archive/PlantVillage_resize_224/PlantVillage_resize_224'

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
    transforms.RandomVerticalFlip(p=0.5)
])


# It's not a language model, so it's not going to know
# the names of the classes, we will just link them later on.

full_dataset = datasets.ImageFolder(DATASET_PATH, transform=transform)

print(f"Dataset name: PlantVillage Resized")
print(f"Number of instances: {len(full_dataset)}")
print(f"Classes: {full_dataset.classes}")
sorted_classes = sorted(full_dataset.classes, key=lambda x: int(x[1:]))
print(f"Sorted classes: {sorted_classes}")

num_samples = min(1900, len(full_dataset))
indices = random.sample(range(len(full_dataset)), num_samples)
subset = Subset(full_dataset, indices)

y = [full_dataset.targets[i] for i in indices]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

train_indices, test_indices = train_test_split(range(len(subset)), test_size=0.2)

train_dataset = Subset(subset, train_indices)
test_dataset = Subset(subset, test_indices)

train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=16)

num_classes = len(sorted_classes)
print("Number of classes:", num_classes)
print("Dataset loaded successfully!")
