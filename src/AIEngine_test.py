"""Import AIEngine for test."""
from AIEngine import AIEngine
import argparse


def get_args():
    """Make the script to accept user input arguments."""
    parser = argparse.ArgumentParser("Parse image & label for AI recognition")
    parser.add_argument("photo", type=str, help="""Dog: xander_1.jpg,
                         xander_2.jpg, xander_3.jpg, xander_4.jpg;
                         Cat: neymar_1.jpg, neymar_2.jpg, neymar_3.jpeg,
                         neymar_4.jpeg; View: iceland_1.jpeg, iceland_2.jpeg,
                         iceland_3.jpeg, iceland_4.jpeg""")
    parser.add_argument("target", type=str, help="""To specify target label to
                         detect, Dog, Cat or view: Antler, Mountain,
                         Nature, River, etc.""")
    parser.add_argument("-pt", "--print_labels", default=True, type=str,
                        help="To print labels detected from the image")
    parser.add_argument("-s", "--show", default=True, type=str,
                        help="Show the bounding boxes for the labels detected")

    args = parser.parse_args()

    return args


def inference_image(args):
    """To use AWS AI for image inference."""
    photo = args.photo
    bucket = 'myawsbucket0723'
    target = args.target
    print_labels = args.print_labels
    show_boxes = args.show
    print("[ Print Info ] To predict {} label...".format(target))
    print("\n----------")
    print("[ Print Info ] {} label detected: {}".format(target,
          AIEngine.detect_labels(photo, bucket, target,
                                 print_labels, show_boxes)))


if __name__ == "__main__":
    args = get_args()
    inference_image(args)
