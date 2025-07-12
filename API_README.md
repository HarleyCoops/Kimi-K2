# Kimi-K2 API Examples with Tool Calling

This directory contains comprehensive examples demonstrating the implementation and utilization of the Kimi-K2 model API with tool calling capabilities. The Kimi-K2 model represents a state-of-the-art mixture-of-experts architecture with 32 billion activated parameters and 1 trillion total parameters, specifically optimized for agentic intelligence and tool utilization.

## Quick Start

### 1. API Key Acquisition
Obtain your API key from the [Moonshot AI Platform](https://platform.moonshot.ai). This key is required for all API interactions and should be treated as a sensitive credential.

### 2. Environment Configuration
```bash
# Windows PowerShell
$env:MOONSHOT_API_KEY="your_api_key_here"

# Linux/Mac
export MOONSHOT_API_KEY="your_api_key_here"
```

### 3. Dependency Installation
```bash
pip install -r requirements.txt
```

### 4. Verification Test
```bash
python quick_test.py
```

## File Structure

- **`quick_test.py`** - Minimal implementation for basic tool calling verification
- **`kimi_k2_api_example.py`** - Comprehensive demonstration of multiple tool calling paradigms
- **`requirements.txt`** - Python package dependencies
- **`API_README.md`** - This documentation file

## Implemented Features

### Tool Calling Paradigms
1. **Non-streaming mode** - Synchronous response processing with complete response aggregation
2. **Streaming mode** - Asynchronous response streaming with real-time token processing
3. **Manual parsing** - Custom tool call extraction for inference engines lacking built-in parsers

### Exemplary Tools
- **Weather Tool** - Simulated meteorological data retrieval for specified urban areas
- **Calculator Tool** - Mathematical expression evaluation with input validation

### API Compatibility Matrix
- **OpenAI-compatible API** - Standard OpenAI client library integration
- **Anthropic-compatible API** - Alternative API specification compliance
- **Temperature mapping** - Normalized temperature scaling: `real_temperature = request_temperature * 0.6`

## Implementation Examples

### Basic Tool Calling Implementation
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.moonshot.ai/v1",
    api_key="your_api_key"
)

# Tool specification
tools = [{
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Perform mathematical calculations",
        "parameters": {
            "type": "object",
            "required": ["expression"],
            "properties": {
                "expression": {"type": "string"}
            }
        }
    }
}]

# API invocation
response = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Instruct",
    messages=[{"role": "user", "content": "Calculate 2 + 2"}],
    tools=tools,
    tool_choice="auto"
)
```

### Streaming Implementation with Tool Integration
```python
response = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Instruct",
    messages=[{"role": "user", "content": "What's 5 * 10?"}],
    tools=tools,
    tool_choice="auto",
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end='')
```

## Tool Call Execution Flow

1. **Request Transmission** - Tool definitions and user query submission
2. **Model Decision** - Autonomous tool selection and parameter determination
3. **Tool Call Extraction** - Response parsing and tool invocation identification
4. **Tool Execution** - Function execution with validated parameters
5. **Result Integration** - Tool output incorporation into conversation context
6. **Iterative Processing** - Continued conversation until completion criteria met

## Tool Definition Schema

```python
tools = [{
    "type": "function",
    "function": {
        "name": "function_name",
        "description": "Function purpose and usage context",
        "parameters": {
            "type": "object",
            "required": ["param1", "param2"],
            "properties": {
                "param1": {
                    "type": "string",
                    "description": "Parameter specification and constraints"
                }
            }
        }
    }
}]
```

## Technical Specifications

- **API Endpoint**: `https://api.moonshot.ai/v1`
- **Model Identifier**: `moonshotai/Kimi-K2-Instruct`
- **Temperature Scaling**: `real_temperature = request_temperature * 0.6`
- **Tool Parsing Requirements**: Inference engine must support Kimi-K2's native tool parser
- **Context Window**: 128K tokens maximum
- **Model Architecture**: 32B activated parameters (1T total parameters)

## Error Resolution

### Common Error Conditions

1. **API Key Authentication Failure**
   ```
   Please set your MOONSHOT_API_KEY environment variable
   ```
   - Resolution: Verify environment variable configuration

2. **Tool Call Parsing Failure**
   ```
   Error: Tool call parsing failed
   ```
   - Resolution: Ensure inference engine supports Kimi-K2 tool parser

3. **Model Resolution Failure**
   ```
   Error: Model not found
   ```
   - Resolution: Confirm model identifier: `moonshotai/Kimi-K2-Instruct`

### Support Resources

- **Technical Documentation**: [Kimi-K2 GitHub Repository](https://github.com/moonshotai/Kimi-K2)
- **API Platform**: [Moonshot AI Platform](https://platform.moonshot.ai)
- **Community Support**: [Discord Community](https://discord.gg/TYU2fdJykW)

## Development Roadmap

1. **Custom Tool Development** - Implementation of domain-specific tool functions
2. **Production Deployment** - Enterprise-grade error handling and monitoring
3. **Performance Optimization** - Streaming, batching, and latency optimization
4. **Self-Hosting Configuration** - Reference the [deployment guide](../docs/deploy_guidance.md) for local deployment

---

*This documentation provides a comprehensive foundation for integrating Kimi-K2's tool calling capabilities into production systems.* 