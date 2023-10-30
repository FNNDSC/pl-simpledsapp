#!/usr/bin/env python                                            
#
# simpledsapp ds ChRIS plugin app
#
# (c) 2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#


import os
import shutil
import time
import json
from pflog import pflog

from chrisapp.base import ChrisApp


Gstr_title = """
     _                 _          _                       
    (_)               | |        | |                      
 ___ _ _ __ ___  _ __ | | ___  __| |___  __ _ _ __  _ __  
/ __| | '_ ` _ \| '_ \| |/ _ \/ _` / __|/ _` | '_ \| '_ \ 
\__ \ | | | | | | |_) | |  __/ (_| \__ \ (_| | |_) | |_) |
|___/_|_| |_| |_| .__/|_|\___|\__,_|___/\__,_| .__/| .__/ 
                | |                          | |   | |    
                |_|                          |_|   |_|    
"""

Gstr_synopsis = """

    NAME

       simpledsapp.py 

    SYNOPSIS

        python simpledsapp.py                                        
            [-h] [--help]                                               
            [--json]                                                   
            [--man]                                                     
            [--meta]                                                    
            [--savejson <DIR>]                                         
            [-v <level>] [--verbosity <level>]                          
            [--version]                                                
            <inputDir>                                                  
            <outputDir> 
            [--prefix <PREFIX>] 
            [--ignoreInputDir]
            [--sleepLength <SECONDS>]
            [--dummyInt <INT>]
            [--dummyFloat <FLOAT>]
            

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-simpledsapp simpledsapp                        \
                /incoming /outgoing

    DESCRIPTION

        `simpledsapp.py` ...

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 
        
        <inputDir> 
        Input directory.
        
        <outputDir> 
        Output directory.
        
        [--prefix <PREFIX>] 
        If specified, append this prefix to resulting output files. 
        
        [--ignoreInputDir]
        If specified, ignore the input dir completely. 
        
        [--sleepLength <SECONDS>]
        If specified, time to sleep before performing plugin action. 
        
        [--dummyInt <INT>]
        If specified, this is a dummy (not used) input integer parameter. 
        
        [--dummyFloat <FLOAT>] 
        If specified, this is a dummy (not used) input float parameter.     
"""


class SimpleDSApp(ChrisApp):
    """
    A simple ChRIS ds app demo
    """
    PACKAGE                 = __package__
    TITLE                   = 'Simple chris ds app'
    CATEGORY                = 'copy'
    TYPE                    = 'ds'
    ICON                    = '' # url of an icon image
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('-p', '--prefix',
                           dest         = 'prefix',
                           type         = str,
                           optional     = True,
                           help         = 'prefix for file names',
                           default      = '')
        self.add_argument('--ignoreInputDir',
                           dest         = 'b_ignoreInputDir',
                           type         = bool,
                           optional     = True,
                           help         = 'if set, ignore the input dir completely',
                           default      = False)
        self.add_argument('--sleepLength',
                           dest         = 'sleepLength',
                           type         = str,
                           optional     = True,
                           help         = 'time to sleep before performing plugin action',
                           default      = '0')
        self.add_argument('--dummyInt',
                           dest         = 'dummyInt',
                           type         = int,
                           optional     = True,
                           help         = 'dummy integer parameter',
                           default      = 1)
        self.add_argument('--dummyFloat',
                           dest         = 'dummyFloat',
                           type         = float,
                           optional     = True,
                           help         = 'dummy float parameter',
                           default      = 1.1)
    @pflog.tel_logTime(
            event       = 'simpledsapp',
            log         = 'A simple ChRIS ds app demo'
    )
    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())

        print('Sleeping for %s' % options.sleepLength)
        time.sleep(int(options.sleepLength))
        if options.b_ignoreInputDir:
            # simply create a timestamp in the output dir
            d_timeStamp = {
                'year':     time.strftime('%Y'),
                'month':    time.strftime('%m'),
                'day':      time.strftime('%d'),
                'hour':     time.strftime('%H'),
                'minute':   time.strftime('%M'),
                'second':   time.strftime('%S'),
            }
            print('Saving timestamp object')
            print(json.dumps(d_timeStamp, indent=4))
            with open('%s/timestamp.json' % options.outputdir, 'w') as f:
                json.dump(d_timeStamp, f, indent=4)
        else:
            for (dirpath, dirnames, filenames) in os.walk(options.inputdir):
                relative_path = dirpath.replace(options.inputdir, "").strip("/")
                output_path = os.path.join(options.outputdir, relative_path)
                for dirname in dirnames:
                    print('Creating directory... %s' % os.path.join(output_path, dirname))
                    os.makedirs(os.path.join(output_path, dirname))
                for name in filenames:
                    new_name = options.prefix + name
                    str_outpath = os.path.join(output_path, new_name)
                    print('Creating new file... %s' % str_outpath)
                    shutil.copy(os.path.join(dirpath, name), str_outpath)

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
