# Photoshop Super Resolution :mag:
<p align="center"><b>A user-friendly script to use srgan for upscaling images directly inside photoshop.</b></p>

![Photoshop Menu](Upscale_comparison.jpg?raw=true)

# Requirements
Based on the super resolution repository the machine learning solution requires tensorflow and tensorlayer to be installed on your python environment.

* Therefore there is "**requirements.txt**" that includes all the required libraries and can be installed simply by running this pip command
`pip install -r requirements.txt`
* Make sure to have **python.exe** and **scripts/pip.exe** is already in your system **PATH** environment variable.
* This solution is using **tensorflow-gpu** which requires by default to have a supporting **CUDA GPU** and **cuDNN** installed.
* If you are going to install the same **tensorflow-gpu** and **tensorlayer** versions that are mentioned in the requirement.txt file we recommend to use **CUDA v9.0** with the compatible version of **cuDNN**.
* In case of not having a supporting GPU, you can still use tensorflow the cpu version but the image processing time will be longer.

# Installation
![Photoshop Menu](Photoshop_menu.jpg?raw=true)
* After fulfilling the requirements all what you need is just to copy the **Presets** folder inside your photoshop root directory and accept the overwriting.
* Restart your photoshop if you have a running session already.
* Run the script from `File > Scripts > [3Deep] SuperResolution`.

# Links
* cuDNN | https://developer.nvidia.com/cudnn
* CUDA | https://developer.nvidia.com/cuda-toolkit-archive

# Authors
* Photoshop script (.jsx and .py) [3deep.org](https://www.3deep.org) | author [Mahmoud Hesham](https://github.com/MahmoudHesham).
* Super Resolution Repository ["Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network"](https://github.com/tensorlayer/srgan) | author [zsdonghao](https://github.com/zsdonghao). 

# License
* For academic and non-commercial use only.
* For commercial use, please contact contact@3deep.org and they will check the ability of using it commercially with the solution author.
