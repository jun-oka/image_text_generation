#coding:utf-8;
from inspect_caffe_net import get_img_label
from text_generation import make_random_text
import argparse


parser = argparse.ArgumentParser(
    description='Evaluate a Caffe reference model on ILSVRC2012 dataset')
parser.add_argument('image', help='Path to inspection image file')
parser.add_argument('model_type', choices=('alexnet', 'caffenet', 'googlenet'),
                    help='Model type (alexnet, caffenet, googlenet)')
parser.add_argument('model', help='Path to the pretrained Caffe model')
parser.add_argument('--mean', '-m', default='ilsvrc_2012_mean.npy',
                    help='Path to the mean file')
parser.add_argument('--gpu', '-g', type=int, default=-1,
                    help='Zero-origin GPU ID (nevative value indicates CPU)')
args = parser.parse_args()

if __name__ == '__main__':
    model_type = args.model_type
    model = args.model
    img = args.image
    mean = args.mean
    gpu = args.gpu
    #print(model_type, model, img, mean, gpu)

    #label = get_img_label(img, model_type, model, mean, gpu)
    label = "airliner"
    make_random_text(label)
