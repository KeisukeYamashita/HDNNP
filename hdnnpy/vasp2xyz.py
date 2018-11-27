# -*- coding: utf-8 -*-

import ase.io
from pyplelogger.pyplelogger import Logger
log = Logger(__name__).build()

def convert(args):
    images = []

    prefix = args.prefix
    outcar_file = args.outcar
    output = args.output

    log.info("Started converting vasp2xyz...")

    for atoms in ase.io.iread(outcar_file, index=':', format='vasp-out'):
        atoms.info['config_type'] = prefix + atoms.get_chemical_formula()
        images.append(atoms)

    ase.io.write(output, images, format='xyz')
    log.info("Converted {} to {}".format(outcar_file, output))