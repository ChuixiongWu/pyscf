#!/usr/bin/env python
# Copyright 2014-2018 The PySCF Developers. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from pyscf import gto, scf
import pyscf.md.integrator as integrator

h2o = gto.M(atom=[
    ['O', 0,0,0],
    ['H', 0, -0.757, 0.587],
    ['H', 0, 0.757, 0.587]
    ],
    basis='def2-svp')

def tearDownModule():
    global h2o
    del h2o

class KnownValues(unittest.TestCase):
    def test_zero_init_veloc(self):
        hf_scanner = scf.RHF(h2o)
        hf_scanner.conv_tol_grad = 1e-6
        hf_scanner.max_cycle = 700 
        hf_scanner = hf_scanner.nuc_grad_method().as_scanner()

        driver = integrator.VelocityVerlot(hf_scanner, steps=1000, dt=10)
        driver.kernel()        


if __name__=="__main__":
    print("Full Tests for H2O")
    unittest.main()
