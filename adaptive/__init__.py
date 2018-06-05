# -*- coding: utf-8 -*-
from .notebook_integration import (notebook_extension, live_plot,
                                   active_plotting_tasks)

from . import learner
from . import runner

from .learner import (Learner1D, Learner2D, AverageLearner, AverageLearner2D,
                      BalancingLearner, DataSaver, IntegratorLearner)
from .runner import Runner, BlockingRunner
from . import version

__version__ = version.version

del notebook_integration  # to avoid confusion with `notebook_extension`
del version
