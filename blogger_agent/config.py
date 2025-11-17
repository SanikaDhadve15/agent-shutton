# blogger_agent/config.py
# Local development configuration for Agent Shutton
# Works WITHOUT Google Cloud ADC and is fully compatible with ADK Web + tests.

class Config:
    def __init__(self):
        # ---------------------------------------------------------
        # MAIN MODELS USED BY AGENT-SHUTTON
        # ---------------------------------------------------------

        # Root / reasoning model
        self.root_model = "gpt-4o-mini"

        # Critic model for validators (OutlineValidationChecker, BlogPostValidationChecker)
        self.critic_model = "gpt-4o-mini"

        # Temperature for generation
        self.temperature = 0.4

        # Max tokens ADK is allowed to output
        self.max_output_tokens = 2048

        # Local mode — no Google Cloud required
        self.use_cloud = False

        # Project ID (optional, kept for compatibility)
        self.project_id = None


# IMPORTANT: make config an OBJECT, not a dict
config = Config()
