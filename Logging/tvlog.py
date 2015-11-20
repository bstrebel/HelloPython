__author__ = 'bst'

import os

from ConfigParser import ConfigParser
from argparse import ArgumentParser

import logging
import logging.config

class LogFileHandler(logging.FileHandler):
    def __init__(self, path, mode='a', endcoding='utf-8'):
        path = os.path.expanduser(path)
        logging.FileHandler.__init__(self, path, mode, endcoding)


if __name__ == '__main__':

    options = {'opt': 'default value'}

    parser = ArgumentParser(description='TVheadend Toolbox Rev. 0.1 (c) Bernd Strebel')
    parser.add_argument('-c', '--config', type=str, help='alternate configuration file')

    args = parser.parse_args()
    opts = vars(args)


    print options.get('_opt', "n/a")


    #cfgFile = os.path.expanduser('~/.tvlog.cfg')
    cfgFile = os.path.expanduser('tvlog.cfg')

    logging.config.fileConfig(cfgFile)
    logger = logging.getLogger('tvlog')
    logger.info("Logging started ...")

    cfg = ConfigParser({'tvheadend':'xxx'})
    cfg.read(cfgFile)


    print cfg.get('tvlog', 'tvheadend')




