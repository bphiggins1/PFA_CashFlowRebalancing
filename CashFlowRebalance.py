##############################################################################
# CashFlowRebalance.py
##############################################################################
import numpy as np

def cash_flow_rebalancing(w_actual, w_target, B):

  """ Determines the minimum cash deposit amount
  required to move a portfolio back to its target weights.
  
  Parameters
  ----------
  w_actual : a numpy array of current portfolio weights, 
  w_target : a numpy array of target weights 
  B : the current portfolio balance in dollars

  Returns
  -------
  D : deposit amount
  """

  # Assert weights sum to 100% with tolerance of 1 bps
  # If portfolio has leverage then weights could sum to more than 100%
  assert ((np.sum(w_actual) + np.sum(w_target)) - 2) < 0.0001

  # Normalize the most underweight asset to the target weights
  # to determine deposit amount
  D = np.max(w_actual / w_target)*B - B

  # Check
  print('Actual weights', w_actual)
  print('Asset dollar value before deposit', B*w_actual)
  print('Portfolio current balance', B)
  print('Portfolio deposit amount', D)
  print('Asset dollar value after deposit', (B + D)*w_target)
  print('Target weights', w_target)

  return D

# 2 asset test
w_actual = np.array([0.80, 0.20])
w_target = np.array([0.70, 0.30])
B = 90
cash_flow_rebalancing(w_actual, w_target, B)

# 3 asset test
w_actual = np.array([0.55, 0.35, 0.10])
w_target = np.array([0.60, 0.30, 0.10])
B = 100
cash_flow_rebalancing(w_actual, w_target, B)

# 4 asset test
w_actual = np.array([0.69, 0.23, 0.04, 0.04])
w_target = np.array([0.60, 0.22, 0.12, 0.06])
B = 110
cash_flow_rebalancing(w_actual, w_target, B)