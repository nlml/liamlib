import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def plot_img_with_rects(im, rects, edgecolor='r'):
    # Plots an image with bounding boxes superimposed
    fig, ax = plt.subplots(1, figsize=[7, 7])
    # Display the image
    ax.imshow(im)
    for r in rects:
        x, y, x1, y1 = r
        w = x1 - x
        h = y1 - y
        # Create a Rectangle patch
        rect = patches.Rectangle((x, y), w, h, linewidth=3, edgecolor=edgecolor, facecolor='none')
        # Add the patch to the Axes
        ax.add_patch(rect)
    plt.show()


def make_labelimg_xml(imgfilename, boxes):
    out = '\n<annotation>\n    <folder>labelimgtest</folder>\n    <filename>2019-03-01_000001.png</filename>\n    <path>/home/liam/labelimgtest/2019-03-01_000001.png</path>\n    <source>\n        <database>Unknown</database>\n    </source>\n    <size>\n        <width>474</width>\n        <height>621</height>\n        <depth>3</depth>\n    </size>\n    <segmented>0</segmented>'  # noqa
    for i, b in enumerate(boxes):
        out += '\n\t<object>\n\t\t<name>{0}</name>\n\t\t<pose>Unspecified</pose>\n\t\t<truncated>0</truncated>\n\t\t<difficult>0</difficult>\n\t\t<bndbox>\n\t\t\t<xmin>{1}</xmin>\n\t\t\t<ymin>{2}</ymin>\n\t\t\t<xmax>{3}</xmax>\n\t\t\t<ymax>{4}</ymax>\n\t\t</bndbox>\n\t</object>\n'.format(i, *b)  # noqa
    out += '\n</annotation>'
    return out


def labelimg_xml_to_json(labelimgxml_path):
    out = []
    tree = ET.parse(labelimgxml_path).getroot()
    for type_tag in tree.findall('object'):
        bndbox = type_tag.find('bndbox')
        bndbox = [int(bndbox.find(i).text) for i in ['xmin', 'ymin', 'xmax', 'ymax']]
        out.append({"id": 0, "bbox": bndbox})
    return out
