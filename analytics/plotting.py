import numpy as np
import matplotlib.pyplot as plt
from services.gateways import DomainGateway

def set_up_servers():
    domain_gate = DomainGateway()
    servers_stats = domain_gate.get_all_servers()
    servers_stats = [list(s) for s in servers_stats]

    filtered_servers = [['Apache', 0], ['nginx', 0]]


    for s in servers_stats:
        if s[0] == None:
            pass

        elif s[0].startswith('Apache'):
            filtered_servers[0][1] += s[1]

        elif s[0].startswith('nginx'):
            filtered_servers[1][1] += s[1]
        
        else:
            filtered_servers.append(s)

    return filtered_servers


def plot(servers):

    height = [i[1] for i in servers]
    bars = [i[0] for i in servers]
    y_pos = np.arange(len(bars))

    plt.barh(y_pos, height)
    plt.yticks(y_pos, bars)
    
    plt.show()


def main_plot():
    servers = set_up_servers()
    plot(servers)