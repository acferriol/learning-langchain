from azure.ai.evaluation import (
    ToolCallAccuracyEvaluator,
    OpenAIModelConfiguration,
)
import rich

model_config: OpenAIModelConfiguration = {
    "api_key": "",
    "base_url": "http://localhost:11434/v1",
    "model": "llama3.2:3b",
    "type": "openai",
}

tool_call_accuracy_evaluator = ToolCallAccuracyEvaluator(model_config=model_config)

score = tool_call_accuracy_evaluator(
    query="How is the weather in New York?",
    response="The weather in New York is sunny.",
    tool_calls={
        "type": "tool_call",
        "tool_call": {
            "id": "call_eYtq7fMyHxDWIgeG2s26h0lJ",
            "type": "function",
            "function": {
                "name": "fetch_weather",
                "arguments": {"location": "New York"},
            },
        },
    },
    tool_definitions={
        "id": "fetch_weather",
        "name": "fetch_weather",
        "description": "Fetches the weather information for the specified location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location to fetch weather for.",
                }
            },
        },
    },
)

rich.print(score)
