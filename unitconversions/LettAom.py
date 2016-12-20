#####################################################################
#                                                                   #
# Power supplies for lett lab                                       #
# Added 8/1/2016 by zach glassman                                   #
#                                                                   #
# Copyright 2013, Monash University                                 #
#                                                                   #
# This file is part of the labscript suite (see                     #
# http://labscriptsuite.org) and is licensed under the Simplified   #
# BSD License. See the license.txt file in the root of the project  #
# for the full license.                                             #
#                                                                   #
#####################################################################
from __future__ import division

from UnitConversionBase import *
from numpy import int16


class AOMConvert(UnitConversion):
    base_unit = 'V'
    derived_units = ['MHz']

    def __init__(self, calibration_parameters = None):
        self.parameters = calibration_parameters
        # I[A] = slope * V[V] + shift
        # Saturates at saturation Volts
        self.parameters.setdefault('slope', 1) # A/V
        self.parameters.setdefault('shift', 0) # A
        self.parameters.setdefault('v_min',0) # V
        self.parameters.setdefault('v_max',5)

        UnitConversion.__init__(self,self.parameters)
        # We should probably also store some hardware limits here, and use them accordingly
        # (or maybe load them from a globals file, or specify them in the connection table?)

    def MHz_to_base(self,amps):
        #here is the calibration code that may use self.parameters
        volts = (amps - self.parameters['shift']) / self.parameters['slope']
        return volts


    def MHz_from_base(self,volts):
        volts = volts
        amps = self.parameters['slope'] * volts + self.parameters['shift']
        return amps
