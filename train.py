import sys
sys.path.append('/workspace/mnt/group/face-det/zhubin/caffe/python')
import caffe
caffe.set_device(0)
caffe.set_mode_gpu()
solver = caffe.SGDSolver('solver.prototxt')
solver.net.copy_from('/workspace/mnt/group/face-det/zhubin/train_file/initial.caffemodel')
solver.solve()
