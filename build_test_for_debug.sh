#!/bin/bash
PYTORCH_PATH="$HOME/projects/pytorch/"
eval "$(conda shell.bash hook)"
conda activate tf2
pushd $PYTORCH_PATH
python setup.py clean
PATH=/usr/lib/ccache/:$PATH DEBUG=1 BUILD_TEST=1 USE_DISTRIBUTED=0 USE_MKLDNN=0 USE_CUDA=0 USE_FBGEMM=0 USE_NNPACK=0 USE_QNNPACK=0 USE_XNNPACK=0 BUILD_CAFFE2_OPS=OFF MAX_JOBS=3 CC=clang-7 CXX=clang++-7 python setup.py develop
popd
conda deactivate
