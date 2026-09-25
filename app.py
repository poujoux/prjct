import os
import joblib
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier

plants = ["cactus", "rose"]

info = []
plantforinfo = []

for plant in plants:
    imgdir = os.path.join(plant, "")

    for i in os.listdir(imgdir):
        data = []

        img = Image.open(os.path.join(imgdir, i))
        img = img.convert("RGB")
        img = img.resize((40,40))

        for i in img.getdata():
            data.extend(i)

        info.append(data)
        plantforinfo.append(plant)



print(19*"YOUR MOM")

model = KNeighborsClassifier(n_neighbors=3)
model.fit(info, plantforinfo)

dm = joblib.dump(model, "model.pkl")
