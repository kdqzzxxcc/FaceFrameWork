from distutils.core import setup 
import py2exe

setup(windows=[{"script":"main_windows.py"}], options={"py2exe":{"includes":["sip", "numpy","cv2","PyQt4"]}},
      data_files=[('temp',['./temp/default.jpg'])]
      )