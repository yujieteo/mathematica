import numpy as np
import pandas as pd

p_init = np.array([1/3., 1/3., 1/3.]);

assert p_init.sum() == 1;

p_transition = np.array(
    [[0.90, 0.05, 0.05],
     [0.01, 0.85, 0.14],
     [0.06, 0.04, 0.9]]
)

p_stationary = np.array(
        [[1.0, 0, 0],
        [0.01,0.85,0.14],
        [0.06,0.04,0.9]]
)

p_state_t = [p_init];

for i in range(3):
    assert p_transition[i, :].sum() == 1;

# ergodicity of range? how to know order of magnitude for stationary distribution? magnitude of second largest eigenvalue? see horn and johnson? convergence of chain.

for i in range(100):
    p_state_t.append(p_state_t[-1] @ p_transition);

state_dist = pd.DataFrame(p_state_t);

# idempotency of transition matrix?

print(state_dist);

for i in range(100):
    p_state_t.append(p_state_t[-1] @ p_stationary);

state_dist = pd.DataFrame(p_state_t);

# irreducibility has to do with linear algebra, rank of the matrix is lower than expected. note rank is not well defined in this case

print(state_dist);

