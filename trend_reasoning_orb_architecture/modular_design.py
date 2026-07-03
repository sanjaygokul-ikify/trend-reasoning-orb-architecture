import logging

# Create a logger
logger = logging.getLogger(__name__)

class ModularDesignExample:
    def __init__(self):
        self.logger = logger

    def perform_modular_task(self) -> None:
        try:
            # Implement modular task logic here
            self.logger.info("Performing modular task...")
            # Simulate some task execution time
            import time
            time.sleep(1)
            self.logger.info("Modular task completed successfully")
        except Exception as e:
            self.logger.error(f"Error performing modular task: {str(e)}")


# Example usage
if __name__ == "__main__":
    modular_design_example = ModularDesignExample()
    modular_design_example.perform_modular_task()