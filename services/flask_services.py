from services.gateways import DomainGateway


def json_data():
    domain_gate = DomainGateway()
    servers_stats = domain_gate.get_all_servers()
    servers_dict = dict((x,y) for x,y in servers_stats)
    del servers_dict[None]
    
    return servers_dict
