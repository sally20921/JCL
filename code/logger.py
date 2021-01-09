import os
import logging 

from tqdm import tqdm
from tensorboardX import SummaryWriter
from tensorboard import default, program
import tensorflow as tf

from utils import get_dirname_from_args, get_now

