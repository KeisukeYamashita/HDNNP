# -*- coding: utf-8 -*-

from pathlib import Path
import ase.io
from pyplelogger.pyplelogger import Logger
log = Logger(__name__).build()
 
def merge(args):
    step = args.step
    inputs = args.inputs
    output = args.output

    log.info("Started merging xfz files...")
    
    for file in inputs.glob('*.xyz'):
        images = ase.io.read(file, index='::{}'.format(step), format='xyz')
        ase.io.write(output, images, format='xyz', append=True)

    log.info("Merged files to {}".format(output))