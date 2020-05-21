import numpy as np
import matplotlib.pyplot as plt
from services.gateways import DomainGateway


domain_gate = DomainGateway()
servers_stats = domain_gate.count_servers()


height = [i[1] for i in servers_stats]
bars = [i[0] for i in servers_stats]
y_pos = np.arange(len(bars))
 
plt.barh(y_pos, height)
 
plt.yticks(y_pos, bars)
 
plt.show()
