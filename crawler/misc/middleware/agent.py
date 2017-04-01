# -*- coding: utf-8 -*-

from ..mobile_agents import AGENTS

import random


class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent
