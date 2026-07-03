from typing import List, Dict, Any
from logging import getLogger
from .__init__ import Executor
from packages.core.engine import ReasoningEngine
from packages.core.types import Decision, Context, State

logger = getLogger(__name__)

class Executor:
    def __init__(self, engine: ReasoningEngine):
        self.engine = engine

    def execute(self, input_data: Dict[str, Any]) -> List[Decision]:
        try:
            # Create a list to store the decisions
            decisions = []
            # Loop through the input data and make decisions
            for data in input_data:
                decision = self.engine.decide(data)
                decisions.append(decision)
            # Log the execution process
            logger.info(f'Executed decisions: {decisions}')
            return decisions
        except Exception as e:
            # Handle any exceptions that occur during execution
            logger.error(f'Error executing decisions: {e}')