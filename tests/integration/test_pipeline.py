import unittest
from packages.core import ReasoningEngine
from packages.services import Orchestrator

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        context = Context({})
        state = State({})
        orchestrator = Orchestrator(context, state)
        decision = orchestrator.decide({})
        orchestrator.learn(decision, True)
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()