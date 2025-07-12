# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Development Commands

### Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Configure API key
python setup_api_key.py
```

### Running Examples
```bash
# Basic API test
python quick_test.py

# Comprehensive API examples with tool calling
python kimi_k2_api_example.py
```

## Code Architecture

### API Integration Architecture
This repository implements a client library for the Kimi-K2 language model API. The architecture follows these patterns:

1. **OpenAI-Compatible Interface**: All API interactions use the OpenAI Python client library with custom base_url pointing to `https://api.moonshot.ai/v1`

2. **Tool Calling Paradigm**: The codebase emphasizes tool/function calling capabilities with three implementation approaches:
   - Non-streaming mode with synchronous responses
   - Streaming mode with real-time token processing
   - Manual parsing for inference engines without built-in parsers

3. **Environment-Based Configuration**: API keys are managed through environment variables (`MOONSHOT_API_KEY`) with `.env` file support

### Key Implementation Details

- **Temperature Scaling**: The Anthropic-compatible API applies `real_temperature = request_temperature * 0.6`
- **Model Identifier**: Always use `moonshotai/Kimi-K2-Instruct` for the instruction-tuned model
- **Tool Parser**: When deploying, use `--tool-call-parser kimi_k2` flag for proper tool call parsing
- **Context Window**: Maximum 128K tokens

### Tool Call Flow
1. Define tools using OpenAI function schema format
2. Pass tools array to chat completion request
3. Check `finish_reason` for "tool_calls"
4. **IMPORTANT**: Append assistant message to messages list before processing tool calls
5. Execute tools using `tool_function(**tool_call_arguments)` (unpack arguments)
6. Append tool results with `role="tool"`
7. Continue conversation until completion

### Critical Implementation Notes
- **Function Calling Pattern**: Use `tool_function(**tool_call_arguments)` to unpack the arguments dictionary
- **Streaming Mode**: Must append assistant message with tool calls to messages list before processing
- **Official Guidance Bug**: The documentation shows `tool_function(tool_call_arguments)` but this is incorrect for functions with individual parameters

### Deployment Considerations
The model supports deployment on:
- vLLM (with Tensor Parallelism or Data+Expert Parallelism)
- SGLang (with TP or DP+EP configurations)
- KTransformers (CPU optimization with AMX)
- TensorRT-LLM (multi-node inference)

Note: The model reuses DeepSeekV3CausalLM architecture but uses `"model_type": "kimi_k2"` in config.json for proper optimization.

## Mathematical Notation

The repository uses LaTeX/KaTeX mathematical notation in documentation:
- Inline math: `$x = y$` renders as $x = y$
- Display math: `$$W \leftarrow W - \eta \nabla W$$` renders as centered equation
- GitHub now supports mathematical rendering natively in markdown files
- Use proper mathematical symbols: $\times$, $\leftarrow$, $\nabla$, $\sqrt{}$, etc.