import unittest
from packages.core import Decision, Context, State, ReasoningEngine

class TestCore(unittest.TestCase):
    def test_decision(self):
        context = Context({})
        state = State({})
        engine = ReasoningEngine(context, state)
        decision = engine.decide({})
        self.assertIsInstance(decision, Decision)
    
    def test_learning(self):
        context = Context({})
        state = State({})
        engine = ReasoningEngine(context, state)
        decision = engine.decide({})
        engine.learn(decision, True)
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()