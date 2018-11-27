# -*- coding: utf-8 -*-

from pathlib import Path
import ase.io
 
def merge(args):
    step = int(args.step)
    inputs = args.inputs
    output = args.output

    for f in Path(inputs).glob('*.xyz'):
        images = ase.io.read(f, index='::{}'.format(step), format='xyz')
        ase.io.write(output, images, format='xyz', append=True)