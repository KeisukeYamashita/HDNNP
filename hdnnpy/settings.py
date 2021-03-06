# -*- coding: utf-8 -*-

"""
    hdnnpy.settings

    :copyright: © 2018 by KeisukeYamashita.
    :license: MIT, see LICENSE for more details.
"""

from pathlib import Path
import os
import sys
from mpi4py import MPI
import chainermn

import hdnnpy.argparser as argparser
from pyplelogger.pyplelogger import Logger
log = Logger(__name__).build()


class Settings:
    class file:
        out_dir = 'output'
    class mpi:
        comm = MPI.COMM_WORLD
        rank = MPI.COMM_WORLD.Get_rank()
        size = MPI.COMM_WORLD.Get_size()
        chainer_comm = chainermn.create_communicator('naive', MPI.COMM_WORLD)
    class dataset:
        config = ['all']
        ratio = 0.9
    class model:
        interval = 10
        patients = 5
        init_lr = 1.0e-3
        final_lr = 1.0e-6
        lr_decay = 0.0e-6
        l1_norm = 0.0e-4
        l2_norm = 0.0e-4
        metrics = 'validation/main/tot_RMSE'
    class skopt:
        pass

def load_user_settings(args):
    log.info("Loading user settings...")

    if args.mode == 'train' and args.resume:
        search_path = str(args.resume.parent.absolute())
    elif args.mode in ['prediction', 'phonon']:
        search_path = str(args.masters.parent.absolute())
    else:
        search_path = os.getcwd()
    
    if not Path(search_path, 'configs.py').exists():
        raise FileNotFoundError('`configs.py` is not found in {}'.format(search_path))
    
    sys.path.insert(0, search_path)
    from configs import stg

    # convert path string to pathlib.Path object
    stg.file.out_dir = Path(stg.file.out_dir)
    stg.dataset.xyz_file = Path(stg.dataset.xyz_file)

    log.info("Successfully loaded user settings")

    return stg


def load_phonopy_settings():
    sys.path.insert(0, os.getcwd())
    import phonopy_configs
    return phonopy_configs


args = argparser.parse()
stg = load_user_settings(args)

if args.mode == 'phonon':
    phonopy = load_phonopy_settings()

if not args.debug and stg.mpi.rank != 0:
    sys.stdout = Path(os.devnull).open('w')

file = stg.file
mpi = stg.mpi
dataset = stg.dataset
model = stg.model
skopt = stg.skopt
