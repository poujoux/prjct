import os
import joblib
from PIL import Image

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


dm = joblib.dump(info, "model.pkl")[0]
dm = joblib.load(dm)



if __name__ == "__main__":
    print(19*"YOUR MOM")
    print(dm)


