import joblib
from PIL import Image

# Load model
m = joblib.load("model.pkl")

# Open and preprocess image
img = Image.open(path)
img = img.convert("RGB")
img = img.resize((40, 40))

# Flatten pixel values into one list
data = []
for pixel in img.getdata():
    data.extend(pixel)

# Model prediction
prediction = m.predict([data])

print(prediction)

