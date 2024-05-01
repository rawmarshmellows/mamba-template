mamba create -n mamba-template python=3.12
conda config --add channels conda-forge
conda config --set channel_priority strict

# Setup Ruff
# install the VSCode extension so Ruff can be configured via .vscode/settings.json, you can check that it is using the correct Ruff binary by checking the Ruff logs in the Output tab
mamba install ruff      




# Jupyter notebook setup
mamba install jupyterlab_code_formatter jupyterlab jupyterlab_vim
To setup Jupyter Notebook with Ruff
https://gist.github.com/jbwhit/eecdd1cac2756df85ad165f437445b0b



# Mypy VSCode setup
mamba install mypy
Install MS VSCode extension

# pytest setup
mamba install pytest pytest-watch

# install pre-commit
mamba install pre-commit && pre-commit install


### Performance test
```
PYTHONPATH=src/:. python -m cProfile -s tottime tests/performance/ram64_chip_performance_test.py

 72887962 function calls (72887686 primitive calls) in 49.575 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 22139557   17.122    0.000   23.582    0.000 nand_gate.py:9(__call__)
 14969075    6.970    0.000   22.885    0.000 not_gate.py:13(__call__)
  7170482    6.967    0.000   25.497    0.000 and_gate.py:15(__call__)
 22153022    6.467    0.000    6.467    0.000 bits.py:60(__init__)
   648208    5.164    0.000   45.839    0.000 mux_gate.py:26(__call__)
  1944624    3.335    0.000   19.166    0.000 or_gate.py:18(__call__)
   972950    0.997    0.000    1.725    0.000 bits.py:21(__getitem__)
   326656    0.576    0.000   23.890    0.000 bit_register_chip.py:24(__call__)
    20097    0.518    0.000   24.291    0.001 mux16_gate.py:64(__call__)
   969760    0.516    0.000    0.725    0.000 bits.py:267(__iter__)
    20416    0.295    0.000   24.844    0.001 register_chip.py:86(__call__)
   995957    0.214    0.000    0.214    0.000 {built-in method builtins.iter}
    40513    0.108    0.000    0.129    0.000 bits.py:289(from_bits)
   326656    0.061    0.000    0.061    0.000 data_flip_flop_chip.py:28(__call__)
    20097    0.039    0.000    0.247    0.000 dmux_gate.py:21(__call__)
     2552    0.035    0.000   46.777    0.018 ram8_chip.py:88(__call__)
     5742    0.028    0.000   20.850    0.004 mux4way16_gate.py:185(__call__)
     2871    0.026    0.000    0.289    0.000 dmux8way_gate.py:22(__call__)
    20097    0.023    0.000    0.029    0.000 bits.py:91(from_bits)
      319    0.014    0.000   49.519    0.155 ram64_chip.py:243(__call__)
65061/65056    0.011    0.000    0.011    0.000 {built-in method builtins.len}
        1    0.009    0.009   49.570   49.570 ram64_chip_performance_test.py:7(test_ram64_chip)
```

```
PYTHONPATH=src/:. python -m cProfile -s tottime tests/performance/ram64_chip_int_performance_test.py

         10543687 function calls (10543410 primitive calls) in 4.359 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   648208    1.862    0.000    3.779    0.000 mux_gate.py:7(mux_gate)
  5225858    1.077    0.000    1.077    0.000 and_gate.py:6(and_gate)
  1964721    0.432    0.000    0.432    0.000 not_gate.py:5(not_gate)
  1944624    0.421    0.000    0.421    0.000 or_gate.py:6(or_gate)
   326656    0.211    0.000    2.167    0.000 bit_register_chip.py:11(__call__)
    20416    0.125    0.000    2.292    0.000 register_chip.py:25(__call__)
    20097    0.076    0.000    1.940    0.000 mux16_gate.py:5(mux16_gate)
   326656    0.041    0.000    0.041    0.000 data_flip_flop_chip.py:10(__call__)
     2552    0.022    0.000    4.096    0.002 ram8_chip.py:20(__call__)
     5742    0.018    0.000    1.681    0.000 mux4way16_gate.py:5(mux4way16_gate)
     2871    0.016    0.000    1.974    0.001 mux8way16_gate.py:6(mux8way16_gate)
    20097    0.014    0.000    0.026    0.000 dmux_gate.py:8(dmux_gate)
     2871    0.005    0.000    0.032    0.000 dmux8way_gate.py:5(dmux8way_gate)
      319    0.004    0.000    4.325    0.014 ram64_chip.py:20(__call__)
      957    0.004    0.000    0.006    0.000 utils.py:7(int_to_bin_tuple)
       23    0.003    0.000    0.003    0.000 {method 'read' of '_io.BufferedReader' objects}
        1    0.003    0.003    4.336    4.336 ram64_chip_int_performance_test.py:6(test_ram64_chip_int)
```
