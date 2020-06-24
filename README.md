# EnhanceNet

This is a pre-trained implementation of ENet-PAT from "EnhanceNet:
Single Image Super-Resolution through Automated Texture Synthesis" for a
magnification ratio of 4, based on [reference implementation](https://github.com/msmsajjadi/EnhanceNet-Code)

It comes with a requirements file which takes care of installing all necessary packages
using pip.

This implementation provides a more human-readable code and support to base64 encoded images saved as txt files.

If you use this code as part of a publication, please cite original authors:

```
@inproceedings{enhancenet,
  title={{EnhanceNet: Single Image Super-Resolution through Automated Texture Synthesis}},
  author={Sajjadi, Mehdi S. M. and Sch{\"o}lkopf, Bernhard and Hirsch, Michael},
  booktitle={Computer Vision (ICCV), 2017 IEEE International Conference on},
  pages={4501--4510},
  year={2017},
  organization={IEEE},
  url={https://arxiv.org/abs/1612.07919/}
}
```

# How-To

## Upscale images 4x
  - Copy all high-resolution images to the input directory as image file or base64 string file.
  - Go to `main.py` and use one of 4 modes avalibles on `use_model.py` for each image,  
  providing the path of input images and the desired output path.


## Prerequirements:
  - an internet connection (for the first run only, if you do not have all
    packages)
  - python (<http://python.org>)
  - the following packages, which usually come with Python)
      - pip (<https://pip.pypa.io/en/stable/installing/>)
      - virtualenv (`pip install --user virtualenv`)

# Notes

- Due to this project is part of my Final Degree Project, TensorFlow 1.14 (CPU version) is used and the TF
  computation graph is rebuilt for each image. Several warning related with Conv2D layer appears for this reason.
  
-  I tried the migration to Tensorflow 2 and Keras API but I couldn't use correctly pretrained weights.
  Moreover I have tried to create several models without destroying the previous ones 
  and I have been unable to solve the problems caused by the existence of several graphs
  (the undesired modification of the output tensor operations).

- All images in the input folder are upscaled via bicubic interpolation and EnhanceNet-PAT. 
  A large ammount of memory is needed for prevent Out of Memory errors 
  and the program could crash resizing images larger than 512x512.
  The original authors noticed that 1000x1000 input images or more needed a lot of RAM.


- The first run may take a while, since all necessary packages are installed.
  Subsequent runs are much faster and do not necessitate an internet connection.


- This reference implementation does not reflect the runtime performance of our model and is not suitable for
  runtime benchmarks.


For any questions, comments or help to get it to run, please don't hesitate to
mail us: [flugplatzcode@gmail.com](mailto:flugplatzcode@gmail.com)