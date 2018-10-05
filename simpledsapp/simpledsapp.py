#                                                            _
# Simple chris ds app demo
#
# (c) 2016 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os
import shutil
import time

# import the Chris app superclass
from chrisapp.base import ChrisApp


class SimpleDSApp(ChrisApp):
    """
    Add prefix given by the --prefix option to the name of each input file.
    """
    AUTHORS         = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH        = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC        = os.path.basename(__file__)
    EXECSHELL       = 'python3'
    TITLE           = 'Simple chris ds app'
    CATEGORY        = ''
    TYPE            = 'ds'
    DESCRIPTION     = 'A simple chris ds app demo'
    DOCUMENTATION   = 'http://wiki'
    LICENSE         = 'Opensource (MIT)'
    VERSION         = '0.1'
    MAX_NUMBER_OF_WORKERS = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS = 1  # Override with integer value
    MAX_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT = 0  # Override with the maximum number of GPUs, as an integer, for your plugin


    # Fill out this with key-value output descriptive info (such as an output file path
    # relative to the output dir) that you want to save to the output meta file when
    # called with the --saveoutputmeta flag
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        """
        self.add_argument('--prefix', dest='prefix', type=str, optional=False,
                          help='prefix for file names')
        self.add_argument('--sleepLength',
                           dest     = 'sleepLength',
                           type     = str,
                           optional = True,
                           help     ='time to sleep before performing plugin action',
                           default  = '0')
        self.add_argument('--dummyInt',
                           dest     = 'dummyInt',
                           type     = int,
                           optional = True,
                           help     ='dummy integer parameter',
                           default  = 1)
        self.add_argument('--dummyFloat',
                           dest     = 'dummyFloat',
                           type     = float,
                           optional = True,
                           help     ='dummy float parameter',
                           default  = 1.1)

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        time.sleep(int(options.sleepLength))
        print('sleeping for %s' % options.sleepLength)
        for (dirpath, dirnames, filenames) in os.walk(options.inputdir):
            relative_path  = dirpath.replace(options.inputdir, "").strip("/")
            output_path =  os.path.join(options.outputdir, relative_path)
            for dirname in dirnames:
                print('Creating directory... %s' % os.path.join(output_path, dirname))
                os.makedirs(os.path.join(output_path, dirname))
            for name in filenames:
                new_name    = options.prefix + name
                str_outpath = os.path.join(output_path, new_name)
                print('Creating new file... %s' % str_outpath)
                shutil.copy(os.path.join(dirpath, name), str_outpath)
            


# ENTRYPOINT
if __name__ == "__main__":
    app = SimpleDSApp()
    app.launch()
