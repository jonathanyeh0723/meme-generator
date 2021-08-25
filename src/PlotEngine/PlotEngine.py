"""Import modules for data visualization."""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class PlotEngine:
    """Define PlotEngine class."""

    photos_dir = '_data/photos/picked/'

    @classmethod
    def plot(cls, category) -> str:
        """To show images based on category indicated."""
        fig = plt.figure()
        print(f'Number of images: {len(category)}')

        if len(category) == 12:
            fig.set_size_inches(16, 12)
            nrows = 3
            ncols = 4
        else:
            fig.set_size_inches(4, 3)
            nrows = 1
            ncols = 4

        for i in range(0, len(category)):
            ax = plt.subplot(nrows, ncols, i+1)
            ax.axis('Off')
            img_name = category[i]
            ax.set_title(img_name, fontsize=17)
            img = mpimg.imread(cls.photos_dir + img_name)
            plt.imshow(img)
        plt.show()

        return f"Data visualization for images: {category}"
