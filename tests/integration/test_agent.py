from google.adk.evaluation.agent_evaluator import AgentEvaluator
import pytest
import logging
import os

logger = logging.getLogger(__name__)


@pytest.mark.integration
@pytest.mark.skipif(
    os.environ.get("GOOGLE_API_KEY") is None, reason="GOOGLE_API_KEY is not set"
)
@pytest.mark.asyncio
async def test_with_single_test_file():
    """Test the agent's basic ability via a session file."""
    try:
        await AgentEvaluator.evaluate(
            agent_module="advisor",
            eval_dataset_file_path_or_dir="tests/integration/advisor/advisor.test.json",
        )
    except ValueError as e:
        if "Missing key inputs argument" in str(e):
            error_message = (
                "The test failed because the Google AI API key is missing. "
                "Please make sure you have set the GOOGLE_API_KEY environment variable."
            )
            logger.error(error_message)
            pytest.fail(error_message)
        else:
            raise
    except TypeError as e:
        if "'NoneType' has no len()" in str(e):
            error_message = (
                "The test failed likely because the model did not return a valid response, "
                "which resulted in a 'NoneType' error. This can be caused by API issues, "
                "rate limiting, or if the model's response is empty or malformed."
            )
            logger.error(error_message)
            pytest.fail(error_message)
        else:
            # Re-raise for other TypeErrors that are not the one we are looking for.
            raise
    except Exception as e:
        error_message = f"An unexpected error occurred during evaluation: {e}"
        logger.error(error_message)
        pytest.fail(error_message)