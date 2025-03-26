import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from torch.utils.data import Dataset, DataLoader

# Device configuration (use GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Custom dataset class for merging & handling large CSV files
class CSVDataset(Dataset):
    def __init__(self, file1, file2):
        # Load and merge CSV files
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
        self.data = pd.concat([df1, df2], ignore_index=True)  # Merge data

        self.preprocess_data()

    def preprocess_data(self):
        # Encode categorical features
        for column in self.data.columns:
            if self.data[column].dtype == 'object':  # Convert string columns to numeric
                le = LabelEncoder()
                self.data[column] = le.fit_transform(self.data[column])

        # Separate features and target
        self.X = self.data.iloc[:, :-1].values  # Features
        self.y = self.data.iloc[:, -1].values   # Target

        # Normalize features
        scaler = StandardScaler()
        self.X = scaler.fit_transform(self.X)

        # Convert to PyTorch tensors
        self.X = torch.tensor(self.X, dtype=torch.float32)
        self.y = torch.tensor(self.y, dtype=torch.float32).view(-1, 1)  # Reshape for BCE Loss

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# Load dataset and create DataLoader (batch processing)
batch_size = 1024  # Adjust based on memory capacity
dataset = CSVDataset("./code/src/backend/model/HI-Small_Trans.csv", "./code/src/backend/model/LI-Small_Trans.csv")
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=2)

# Define Logistic Regression Model
class LogisticRegression(nn.Module):
    def __init__(self, input_size):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(input_size, 1)
    
    def forward(self, x):
        return torch.sigmoid(self.linear(x))

# Initialize model
input_size = dataset.X.shape[1]
model = LogisticRegression(input_size).to(device)

# Define loss function and optimizer
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)  # Adam optimizer for efficiency

# Training loop
num_epochs = 10
for epoch in range(num_epochs):
    epoch_loss = 0
    for X_batch, y_batch in dataloader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)  # Move data to GPU if available

        # Forward pass
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss / len(dataloader):.4f}')

# Save trained model
torch.save(model.state_dict(), "./code/src/backend/model/optimized_logistic_regression.pth")
print("Model saved successfully!")

# Evaluation
def evaluate_model(model, dataset):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for X_batch, y_batch in DataLoader(dataset, batch_size=batch_size, num_workers=2):
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            y_pred = model(X_batch)
            y_pred_class = (y_pred >= 0.5).float()
            correct += (y_pred_class.eq(y_batch).sum().item())
            total += y_batch.size(0)

    accuracy = correct / total
    print(f'Accuracy: {accuracy * 100:.2f}%')

evaluate_model(model, dataset)

