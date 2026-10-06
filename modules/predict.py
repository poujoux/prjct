from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
import joblib
import os


class EducateIt:

    modulepath = os.path.join("static", "modules", "model.pkl")

    def __init__(self, images, name=""):
        self.images = images
        self.name = name

    def putfiles(self):
        info = []
        plantforinfo = []

        path = os.path.join("static", "images", self.name)

        if os.path.exists(path):
            return -1

        os.makedirs(path)

        for image in self.images:
            filename = image.filename
            filepath = os.path.join(path, filename)

            image.save(filepath)

            data = self.imginfo(filepath)

            info.append(data)
            plantforinfo.append(self.name)

        # Train after all images have been processed
        model = KNeighborsClassifier(n_neighbors=3)
        model.fit(info, plantforinfo)

        joblib.dump(model, modulepath)

        return 0

    def predict(self, image):
        model = joblib.load(modulepath)

        data = self.imginfo(image)

        prediction = model.predict([data])

        return prediction[0]

    def imginfo(self, image_path):
        data = []

        img = Image.open(image_path)
        img = img.convert("RGB")
        img = img.resize((40, 40))

        for pixel in img.getdata():
            data.extend(pixel)

        return data

