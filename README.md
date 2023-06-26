# CCC_image_upscaling_esrgan_img2txt_with_GPT
# Concept  


## A.I with PICO
**We will be working on an AI project with Pico. The project will be equipped with a camera module, Pico will play the role of Ethernet-based data transmission, and we will use the data to build quality data using AI programs and create reusable source and software.**
- AIOT with the latest AI technology  
- A realistic alternative to AI task


# AI Teams 
[김재현](http://github.com/jh941213) |[정유석](https://github.com/dbtjr1103) |
------|------|
Team Member|Team Member|
<img src="https://user-images.githubusercontent.com/112835087/214769736-c6880568-a4f9-42f7-b5d9-3ef466b6a997.jpeg" width="100" height="100">|<img src ="https://user-images.githubusercontent.com/112835087/227434260-00788b7e-16ec-4d71-b2a5-2fa5fff37e6b.png" width="100" height="100">
  
# Computer Environment
비고| LocalPC | Google Colab | Kaggle Notebook |
-----|-------|-------|-------|
GPU | rtx4090 | T4 | P100
RAM | 64GB |13~52GB|13GB|
Storage | 1TB |166GB|73GB| 

# Technology
## Real ESRGAN
 - [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN.git): Training Real-World Blind Super-Resolution with Pure Synthetic Data

![teaser](https://github.com/WiznetAI/CCC_image_upscaling_esrgan_img2txt_with_GPT/assets/132982685/1916e0f5-cdc9-42ec-9aec-3744ddc2e3d6)
##### Generative Adversarial Networks 
![img](https://github.com/WiznetAI/CCC_image_upscaling_esrgan_img2txt_with_GPT/assets/132982685/65510874-aba2-4843-8db9-104af41d8e77)  

## image-captioning
 - [vit-gpt2-image-captioning](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning)img to text with ChatGPT hugging face model  
<img width="501" alt="image-captioning-example" src="https://github.com/WiznetAI/CCC_image_upscaling_esrgan_img2txt_with_GPT/assets/132982685/44d84ee8-04f2-4e52-8fa8-55ef4a0870ba">
#####  Vision Encoder Decoder
<img width="839" alt="vision-encoder-decoder" src="https://github.com/WiznetAI/CCC_image_upscaling_esrgan_img2txt_with_GPT/assets/132982685/32c208ec-0e4f-4cd8-b8ea-78bf19d7b455">    

# Preparation  
LocalPC(GPU cuda setting) , Pico, LAN, Camera Module  

# PipeLine
<img width="172" alt="dddc" src="https://github.com/WiznetAI/CCC_image_upscaling_esrgan_img2txt_with_GPT/assets/132982685/01d8c0e1-011c-4b3e-bcde-637ebe6ec413">


## **how to run?**

```python
#esrgan
!git clone https://github.com/xinntao/Real-ESRGAN.git
```  
**Just git clone and slowly pick up the tutorials file.**

# Expected effect  
> With the success of the above examples, we will be able to create many more examples that combine the fields of IOT and computer vision.

# Examples
