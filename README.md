# image-enhancement
Improving the visual appearance of an image, by upscaling its resolution.

Clone this repository:
```bash
$ git clone https://github.com/thisilfa/image-enhancement.git
```
I recommend you guys to install `opencv-contrib-python` instead of `opencv-python`.

To upscale a single image, just run:
```bash
$ cd image-enhancement
$ python app.py --img_path 'path/to/image.jpg' --model_path 'models/you/want-to/use.pb'
```

args: <br>
`--img_path`: Path to your image <br>
`--model_path`: Path to model, you can find at `image-enhancement/models` <br>
`--model_name`: Model name to use: ['edsr', 'espcn', 'fsrcnn', 'lapsrn']. Just leave it if you use the models from my repo.<br>
`--n_scale`: Number of scale. Just leave it if you use the models from my repo.<br>

For example, i used the butterfly image from `image-enhancement/downscaled` as input image, and applied any models. These output images will be saved at `image-enhancement/result`.

If you would like to read more about these models, I’ve included their names and repo links below:
- EDSR: Enhanced Deep Residual Networks for Single Image Super-Resolution [on github](https://github.com/Saafke/EDSR_Tensorflow)
- ESPCN: Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network (implementation)
- FSRCNN: Accelerating the Super-Resolution Convolutional Neural Network (implementation)
- LapSRN: Fast and Accurate Image Super-Resolution with Deep Laplacian Pyramid Networks (implementation)