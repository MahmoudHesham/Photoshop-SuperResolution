# This script copyrights belong to 3deep.org and the used solutions authors as mentioned.
# And it's available for academic and non-commercial use only.

# this solution is cloned from this repo
# https://github.com/tensorlayer/srgan
# and the copyrights belongs to it's authors as mentioned there

import time, sys, ntpath
import tensorflow as tf
import tensorlayer as tl
from model import SRGAN_g
from utils import *
from config import config, log_config
import tempfile
from send_to_photoshop import send_to_ps
import os

def super_resolution_image(image_path):

    filename = ntpath.basename(image_path)
    filepath = image_path.replace(filename, "")
    scriptpath = os.path.dirname(os.path.realpath(__file__))
    temppath = '{0}\\temp'.format(scriptpath)

    tempname = next(tempfile._get_candidate_names()) + ".jpg"
    output_filename = '{0}\\output_images\\{1}'.format(scriptpath, tempname)

    ###========================== DEFINE MODEL ============================###

    valid_lr_img = get_imgs_fn(filename, filepath)  # if you want to test your own image
    valid_lr_img = (valid_lr_img / 127.5) - 1  # rescale to ［－1, 1]

    t_image = tf.placeholder('float32', [1, None, None, 3], name='input_image')
    net_g = SRGAN_g(t_image, is_train=False, reuse=False)

    ###========================== RESTORE G =============================###

    sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=False))
    tl.layers.initialize_global_variables(sess)
    tl.files.load_and_assign_npz(sess=sess, name='{0}\\g_srgan.npz'.format(scriptpath), network=net_g)

    ###======================= EVALUATION =============================###

    start_time = time.time()
    out = sess.run(net_g.outputs, {t_image: [valid_lr_img]})

    print("took: %4.4fs" % (time.time() - start_time))
    print("[*] save images")
    
    tl.vis.save_image(out[0], output_filename)
    send_to_ps(output_filename)

    # clear temp folder
    ([os.remove(os.path.join(temppath, f)) for f in  os.listdir(temppath)])

if __name__ == '__main__':
    image_path = sys.argv[-1]
    super_resolution_image(image_path)