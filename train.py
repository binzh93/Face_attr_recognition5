import sys
sys.path.append('/workspace/mnt/group/face-det/zhubin/caffe/python')
import caffe
caffe.set_device(1)
caffe.set_mode_gpu()
solver = caffe.SGDSolver('/workspace/mnt/group/face-det/zhubin/Face_attr_recognition5/solver.prototxt')
solver.solve()
