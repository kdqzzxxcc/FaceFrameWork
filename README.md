# FaceFrameWork
A FrameWork For Face Expression Recognition

# 项目简介

``./JAFFE1``是根据``jaffe亚洲女性人脸表情库``提取出来的人脸,[详情点击这里](http://www.kasrl.org/jaffe.html)

``./data``下``all_names.txt all_labels.txt``是上述数据库每张图片的名字和对应表情的标签

这里共有7种表情，分表代表``NEU = 0; HAP = 1; SAD = 2; SUR = 3; ANG = 4; DIS = 5; FEA = 6;``

``train.csv label.csv``是经过``gabor filter & pca``之后提取出来的``213*213``的数据和标签，用于训练``svm``

``./model``用于存放训练后的``pca & svm & haar``模型，由于太大，我没上传对应的``npy``文件，可以在本地生成一次即可

``detect_face.py``用于对一张输入的图片进行``人脸检测``，使用的是``opevcv``自带的``haarcascade_frontalface``检测器,同时将检测到的图片``scale``到``48*48``用于输入

``display_result.py``用于显示右边界面

``main_algorithm.py``主要算法，分别有``gabor filter, pca, svm``

``main_camera.py``主要用于将调用``opencv camera``得到的``queryframe``用``pyqt widget``展示

``main_windows.py``集成上述所有模块，并显示

# 打包

打包成exe, 进入工程目录， ``python setup.py py2exe`` 即可

也可以使用``Pyinstaller``

PS:引入``sklearn``之后导致``py2exe``以及``pyinstaller``打包之后无法运行，正在解决中

# requirements

opencv

PyQt4

sklearn

numpy

pandas

PIL

# 使用

首先进入运行``python main_algorithm.py``用来生成pca,svm模型存储到``./model``文件夹下

然后运行``python main_windows.py``启动界面

每次点击``photo``拍照之后，会在右下角``label``处得到识别的表情结果

PS:程序非常简陋，非常欢迎大家指点交流 ``kongdq1992@gmail.com``
