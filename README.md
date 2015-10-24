# FaceFrameWork
A FrameWork For Face Expression Recognition

# py2exe

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