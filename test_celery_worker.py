#!/usr/bin/env python
from tasks.server import get_server_info

for i in range(1, 100):
    get_server_info.delay(f'192.168.0.{i}', f'server-{i}')
