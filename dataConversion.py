import os
import xml.etree.ElementTree as ET

# Function to convert XML annotations to YOLO format
def xml_to_yolo(xml_file, class_dict):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    size = root.find('size')
    w = float(size.find('width').text)
    h = float(size.find('height').text)

    yolo_labels = []

    for obj in root.iter('object'):
        class_name = obj.find('name').text
        class_id = class_dict.get(class_name)
        if class_id is None:
            continue  # Skip if the class is not defined in class_dict
        bbox = obj.find('bndbox')
        xmin = float(bbox.find('xmin').text)
        ymin = float(bbox.find('ymin').text)
        xmax = float(bbox.find('xmax').text)
        ymax = float(bbox.find('ymax').text)

        x_center = (xmin + xmax) / (2 * w)
        y_center = (ymin + ymax) / (2 * h)
        width = (xmax - xmin) / w
        height = (ymax - ymin) / h

        yolo_labels.append(f"{class_id} {x_center} {y_center} {width} {height}")

    return yolo_labels

# Define your class dictionary
class_dict = {"Car": 0, "Lane Marker": 1, "Light Pole": 2, "Barrier": 3}  # Update with your actual class labels

# Directory containing XML annotations
xml_dir = "path/to/xml_annotations"

# Directory to save YOLO format labels
yolo_labels_dir = "path/to/yolo_annotations"
os.makedirs(yolo_labels_dir, exist_ok=True)

# Convert each XML annotation to YOLO format and save
for xml_file in os.listdir(xml_dir):
    if xml_file.endswith(".xml"):
        xml_path = os.path.join(xml_dir, xml_file)
        yolo_labels = xml_to_yolo(xml_path, class_dict)
        with open(os.path.join(yolo_labels_dir, os.path.splitext(xml_file)[0] + ".txt"), "w") as f:
            for label in yolo_labels:
                f.write(label + "\n")
