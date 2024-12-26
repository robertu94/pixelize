import PIL.Image
import pathlib
import argparse
import numpy as np
from sklearn.cluster import KMeans

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_image", type=pathlib.Path)
    parser.add_argument("--bits", default=16, type=int)
    parser.add_argument("--colors", default=4, type=int)
    parser.add_argument("--show", action="store_true")
    return parser.parse_args()

def process_image(image: pathlib.Path, bits: int, colors: int, show: bool):
    with PIL.Image.open(image) as img:
        #scale the image
        scaled = img.resize((bits, bits))
        array = np.array(scaled)

        #simplify the colors
        kmeans = KMeans(n_clusters=colors, random_state=0)
        cluster_ids = kmeans.fit_predict(array.reshape(bits*bits, 3))

        # convert back to image to check conversion to show the debug output
        if(show):
            cluster_values = kmeans.cluster_centers_
            cluster_values = cluster_values.astype(np.uint8)
            remapped = np.array([cluster_values[i] for i in cluster_ids]).reshape(bits, bits, 3)
            simplified = PIL.Image.fromarray(remapped)
            simplified.show()

        # produce the output to stdout that Matthew wants
        values = cluster_ids.reshape(bits, bits)
        print('[', end='')
        for row in range(bits):
            print('[', end='')
            for col in range(bits):
                  print(values[row,col], end="," if col != (bits - 1) else "")
            print(']', end=',\n' if row != (bits-1) else "")
        print(']', end='')


def main():
    args = parse_args()
    process_image(args.input_image, args.bits, args.colors, args.show)
    


if __name__ == "__main__":
    main()
