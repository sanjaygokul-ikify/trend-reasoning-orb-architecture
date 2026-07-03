from packages.core import ReasoningEngine

class Orchestrator:
    def __init__(self, context, state):
        self.engine = ReasoningEngine(context, state)
    
    def decide(self, input_data):
        return self.engine.decide(input_data)
    
    def learn(self, decision, outcome):
        return self.engine.learn(decision, outcome)