import re
import cv2
import time
import argparse
from cv2 import dnn_superres

parser = argparse.ArgumentParser(description="Upscaling an image with specific CNN model from OpenCV.")
parser.add_argument('--img_path', type=str, help="Image path to upscale")
parser.add_argument('--model_path', type=str, help="Model path to use")
parser.add_argument('--model_name', type=str, help="Model name to use: ['edsr', 'espcn', 'fsrcnn', 'lapsrn']. If None will be extracted from model_path")
parser.add_argument('--n_scale', type=int, help="Number of scale. If None will be parse from model_path")

args = parser.parse_args()

img_path = args.img_path
model_path = args.model_path
model_name = args.model_name
n_scale = args.n_scale

def preprocessing(img_path, model_path, model_name=None, n_scale=None):

    filename = f"{img_path.split('/')[-1]}"
    start_time = time.time()

    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    if model_name is None:
        model_name = model_path.split('/')[-2]

    if n_scale is None:
        n_scale = re.search(r'x(\d+)', model_path)
        n_scale = int(n_scale.group(1))
        
    superres = dnn_superres.DnnSuperResImpl_create()
    superres.readModel(model_path)
    superres.setModel(model_name, n_scale)
    
    img_rgb = superres.upsample(img_rgb)
    
    print(f"Processing {img_path} in: {round((time.time() - start_time), 2)} sec.\n====")
    cv2.imwrite(f"result/{filename.split('_')[0]}_{model_path.split('/')[-1].split('.')[0]}.jpg", cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))

preprocessing(img_path, model_path, model_name=model_name, n_scale=model_name)