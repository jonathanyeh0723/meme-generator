"""Import modules for data visualization."""
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


photos_dir = '_data/photos/picked/'
photos_list = os.listdir(photos_dir)

dog_photos = []
cat_photos = []
view_photos = []
for p in photos_list:
    if p.startswith('x'):
        dog_photos.append(p)
    elif p.startswith('n'):
        cat_photos.append(p)
    else:
        view_photos.append(p)

cat_photos = sorted(cat_photos)
dog_photos = sorted(dog_photos)
view_photos = sorted(view_photos)
new_photos_list = dog_photos + cat_photos + view_photos


class PlotEngine:
    """Define PlotEngine class."""

    @classmethod
    def plot(cls) -> str:
        """To show all images used to generate meme."""
        fig = plt.figure()
        fig.set_size_inches(16, 12)

        nrows = 3
        ncols = 4

        for i in range(0, len(new_photos_list)):
            ax = plt.subplot(nrows, ncols, i+1)
            ax.axis('Off')
            img_name = new_photos_list[i]
            ax.set_title(img_name, fontsize=10)
            img = mpimg.imread(photos_dir + img_name)
            plt.imshow(img)
        plt.show()

        return "Data visualization for images: {}".format(new_photos_list)
