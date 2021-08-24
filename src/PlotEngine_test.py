"""Import PlotEngine."""
from PlotEngine import PlotEngine
import argparse
import os


def get_photos():
    """To get all photos for data visualization."""
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
    all_photos = dog_photos + cat_photos + view_photos

    return cat_photos, dog_photos, view_photos, all_photos


def args_get():
    """To use argparse to have console accept user input."""
    parser = argparse.ArgumentParser("Parse a photo set to view data")
    parser.add_argument("-ps", "--photo_set", required=True,
                        type=str, help="The name of photo set")
    args = parser.parse_args()

    return args


def plot_decision(cat_photos, dog_photos, view_photos, all_photos, args):
    """To decide a plot category."""
    if args.photo_set == 'cat_photos':
        print(PlotEngine.plot(cat_photos))
    elif args.photo_set == 'dog_photos':
        print(PlotEngine.plot(dog_photos))
    elif args.photo_set == 'view_photos':
        print(PlotEngine.plot(view_photos))
    else:
        print(PlotEngine.plot(all_photos))


if __name__ == "__main__":
    cat_photos, dog_photos, view_photos, all_photos = get_photos()
    args = args_get()
    plot_decision(cat_photos, dog_photos, view_photos, all_photos, args)
