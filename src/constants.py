from skimage import io, transform
import os
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time
from PIL import Image, ImageDraw, ImageFont
from shutil import rmtree
import math
import queue
from shutil import copyfile
import sys
import platform
from random import shuffle
import random
from tqdm import trange, tqdm
import colorsys
from pathlib import Path
from collections import defaultdict, OrderedDict
import json
import glob





CWF = Path(__file__)

PROJECT_PATH = str(CWF.parent.parent) + '/'
DATA_PATH = PROJECT_PATH + 'data/'
NUM_WORDS_PER_QUESTION = 10