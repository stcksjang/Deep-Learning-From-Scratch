import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.functions import function_2
from common.gradients import numerical_gradient

numerical_gradient(function_2, np.array([3.0, 4.0]))
