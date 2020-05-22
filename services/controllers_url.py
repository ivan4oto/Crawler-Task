from datetime import datetime
from .gateways import UrlGateway

class UrlController:
    def __init__(self):
        self.gateway = UrlGateway()

    def seconds_convert(self, seconds):
        if seconds <= 59:
            return (seconds,)

        x = seconds//60
        if x >= 1:
            s = seconds - (x*60)
            return (x,s)

    def get_count_and_time(self):
        visited = self.gateway.get_all_visited()

        first = datetime.fromtimestamp(visited[0].time)
        last = datetime.fromtimestamp(visited[-1].time)
        difference = last-first
        difference = difference.total_seconds()

        real_time = self.seconds_convert(int(difference))

        if len(real_time)>1:
            print(f'\n{len(visited)} visited links for the past:')
            print(f'{real_time[0]} minutes and {real_time[1]} seconds')
        else:
            print(f'\n{len(visited)} visited links for the past:')
            print(f'{real_time[0]} seconds')
        

