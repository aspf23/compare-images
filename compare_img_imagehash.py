from PIL import Image
import imagehash


def compare_images():

    # Create the Hash Object of the first image
    img_1_hash = imagehash.whash(Image.open('img1.jpg'))
    print('First image: ' + str(img_1_hash))

    # Create the Hash Object of the second image
    img_2_hash = imagehash.whash(Image.open('img2.jpg'))
    print('Second image: ' + str(img_2_hash))

    # Compare hashes to determine whether the pictures are the same or not
    if img_1_hash == img_2_hash:
        return "The images are the same !"
    return "The pictures are different. The distance is: " + str(img_1_hash - img_2_hash)


print(compare_images())
