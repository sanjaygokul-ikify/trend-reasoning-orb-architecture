import argparse
from packages.core import ReasoningEngine
from packages.utils.logging import setup_logging

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True)
    args = parser.parse_args()
    setup_logging()
    context = Context({})
    state = State({})
    engine = ReasoningEngine(context, state)
    decision = engine.decide({'input': args.data})
    print(f'Decision: {decision}')
if __name__ == '__main__':
    main()