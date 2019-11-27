# ECUSTFD-resized-
# Background
------
Obesity is a medical condition in which excess body fat has accumulated to the extent that it may have a negative effect on health.  Obesity treatment requires the patients to eat healthy food and decrease the amount of daily calorie intake. For those patients, it is helpful that calories can be estimated from photos.
<br><br>
    Many methods based on computer vision have been created to estimate calories. There are three steps in calorie estimation: capturing food image(s), detecting food and calibration object, estimating calorie of each food.
<br><br>
    For those methods, especially deep learning methods, they need a corresponding image dataset to train and test. However, most of the image datasets concentrate on the food detection and just provide different categories of objects, which is not helpful in visual measurement. That's why we create our food image dataset named ECUSTFD(ECUST Food Dataset).
# Introduction
------
ECUSTFD is a free public food image dataset. Our dataset has 19 types of food as shown in the figure . The number of food images is 2978. The number of images and the number of objects for the same type are shown as follows:
<div align="center"><img src="https://github.com/Liang-yc/images4readme/blob/master/food_sample.jpg"></div>
<br><br>
    For a single food portion, we took several groups of images by using smart phones; each group of images contains a top view and a side view of this food. For each image, there is only one coin as calibration object and no more than two foods in it. If there are two food in the same image, the type of one food is different from another. We provide two datasets for researchers: one includes original images and another includes resized images. The size of each image in resized dataset is less than 1000*1000.<br> 
<div align="center"><img src="https://github.com/Liang-yc/images4readme/blob/master/coin%20sides.jpg"></div>
<br><br>
    As you see, the diameter of the One Yuan Coin is 25.0mm. In ECUSTFD, only 2 kinds of plates are used when taking photos: a white plate and a red plate. If you want to use the circle plate as the calibration object, you may need the diameter of each plate.The white plate's diameter is about 20.7cm and its height is about 2.0cm; the red plate's diameter is about 18.7cm and its height is about 2.0cm.
<br><br>
<table>
<thead><tr><th>red plate</th><th>white plate</th></tr></thead>
        <tr>
            <td><a href=""><img width="100%" style="max-width: 30%;max-height:30%;" alt="" src="https://github.com/Liang-yc/images4readme/blob/master/red_plate.JPG" ></a></td>
            <td><a href=""><img width="100%" style="max-width: 30%;max-height:30%;" alt="" src="https://github.com/Liang-yc/images4readme/blob/master/white_plate.JPG" ></a></td>
        </tr>
</table>
<br>


# Assessment
---------
The dataset with original images and no annotations is publicly available at this [BaiduYun](http://pan.baidu.com/s/1dF866Ut). The small image dataset including annotations, volume and quality information is available at this [github](https://github.com/Liang-yc/ECUSTFD-resized-) or [BaiduYun](http://pan.baidu.com/s/1o8qDnXC). 
<br><br>
    For ECUSTFD with original images, we only provide images as referred. But we provide the food's weight information in [ECUSTFD_WEIGHT](http://pan.baidu.com/s/1dF866Ut#list/path=%2Fcalorie%20estimation%2FECUSTFD_origin%2FECUSTFD_WEIGHT&parentPath=%2Fcalorie%20estimation) folder. If you are interested in character recognition, you can use those images. 
<br><br>
    For the small-size ECUSTFD, The annotations of images are saved in the folder named Annotations and images are saved in the JPEGImages folder. `density.xls` saves food's volume and quality information.
# Citation
-------
If you used the code for your research, please cite the paper:
```
@article{liang2017computer,
  title={Computer vision-based food calorie estimation: dataset, method, and experiment},
  author={Liang, Yanchao and Li, Jianhua},
  journal={arXiv preprint arXiv:1705.07632},
  year={2017}
}
```
# Notice
-------
`mix002T(2)` and `mix005S(4)` have not included calibration objects. As they are used in model-training rather than volume estimation experiment, I have not found this problem till now. Please do not use these 2 images for estimation. I'm sorry for my carelessness. (2017/10/23)
