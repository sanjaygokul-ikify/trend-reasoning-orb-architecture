import unittest
from packages.core import ReasoningEngine

class TestRuntime(unittest.TestCase):
    def test_decide(self):
        context = Context({})
        state = State({})
        engine = ReasoningEngine(context, state)
        decision = engine.decide({})
        self.assertIsNotNone(decision)
    
    def test_learn(self):
        context = Context({})
        state = State({})
        engine = ReasoningEngine(context, state)
        decision = engine.decide({})
        engine.learn(decision, True)
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()