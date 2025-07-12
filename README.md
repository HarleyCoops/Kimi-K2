<div align="center">
  <picture>
      <img src="figures/kimi-logo.png" width="30%" alt="Kimi K2: Open Agentic Intelligence">
  </picture>
</div>

<hr>

<div align="center" style="line-height:1">
  <a href="https://www.kimi.com" target="_blank"><img alt="Chat" src="https://img.shields.io/badge/🤖%20Chat-Kimi%20K2-ff6b6b?color=1783ff&logoColor=white"/></a>
  <a href="https://www.moonshot.ai" target="_blank"><img alt="Homepage" src="https://img.shields.io/badge/Homepage-Moonshot%20AI-white?logo=Kimi&logoColor=white"/></a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://huggingface.co/moonshotai" target="_blank"><img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Moonshot%20AI-ffc107?color=ffc107&logoColor=white"/></a>
  <a href="https://twitter.com/kimi_moonshot" target="_blank"><img alt="Twitter Follow" src="https://img.shields.io/badge/Twitter-Kimi.ai-white?logo=x&logoColor=white"/></a>
    <a href="https://discord.gg/TYU2fdJykW" target="_blank"><img alt="Discord" src="https://img.shields.io/badge/Discord-Kimi.ai-white?logo=discord&logoColor=white"/></a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://github.com/moonshotai/Kimi-K2/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/License-Modified_MIT-f5de53?&color=f5de53"/></a>
</div>

<p align="center">
<b>📰&nbsp;&nbsp;<a href="https://moonshotai.github.io/Kimi-K2/">Tech Blog</a></b> &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; <b>📄&nbsp;&nbsp;Paper Link (coming soon)</b>
</p>

## 1. Model Introduction

Kimi K2 is a state-of-the-art mixture-of-experts (MoE) language model with 32 billion activated parameters and 1 trillion total parameters. Trained with the Muon optimizer, Kimi K2 achieves exceptional performance across frontier knowledge, reasoning, and coding tasks while being meticulously optimized for agentic capabilities.

### Key Features
- Large-Scale Training: Pre-trained a 1T parameter MoE model on 15.5T tokens with zero training instability.
- MuonClip Optimizer: We apply the Muon optimizer to an unprecedented scale, and develop novel optimization techniques to resolve instabilities while scaling up.
- Agentic Intelligence: Specifically designed for tool use, reasoning, and autonomous problem-solving.

### Model Variants
- **Kimi-K2-Base**: The foundation model, a strong start for researchers and builders who want full control for fine-tuning and custom solutions.
- **Kimi-K2-Instruct**: The post-trained model best for drop-in, general-purpose chat and agentic experiences. It is a reflex-grade model without long thinking.

### Quick Start

Get started with Kimi-K2 in just a few commands using our custom setup tools:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up your API key (professional setup utility)
python3 setup_api_key.py

# 3. Run a quick test
python3 quick_test.py

# 4. Explore comprehensive examples
python3 kimi_k2_api_example.py

# 5. Test tool capabilities and MCP integration
python3 explore_tools.py
```

### Custom Tools We've Built

This repository includes several professionally crafted utilities:

| Tool | Purpose | Features |
|------|---------|----------|
| **`setup_api_key.py`** | Professional API key configuration | • PhD-level academic presentation<br>• Secure credential handling<br>• API key validation<br>• Cross-platform support |
| **`quick_test.py`** | Rapid functionality verification | • Basic tool calling test<br>• Calculator function demo<br>• Error handling validation |
| **`kimi_k2_api_example.py`** | Comprehensive implementation guide | • Non-streaming & streaming modes<br>• Multiple tool examples<br>• Production-ready patterns |
| **`explore_tools.py`** | Advanced tool capability testing | • Custom tool creation patterns<br>• MCP integration examples<br>• Tool chaining demonstrations<br>• System command interfaces |
| **`validate_tool_calling.py`** | Implementation validation | • Official guidance compliance<br>• Function signature testing<br>• Bug detection and reporting |

These tools demonstrate best practices for Kimi-K2 integration and provide production-ready starting points for your own implementations.

## 2. Model Summary

<div align="center">


| | |
|:---:|:---:|
| **Architecture** | Mixture-of-Experts (MoE) |
| **Total Parameters** | $1 \times 10^{12}$ (1T) |
| **Activated Parameters** | $32 \times 10^9$ (32B) |
| **Number of Layers** (Dense layer included) | 61 |
| **Number of Dense Layers** | 1 |
| **Attention Hidden Dimension** | 7168 |
| **MoE Hidden Dimension** (per Expert) | 2048 |
| **Number of Attention Heads** | 64 |
| **Number of Experts** | 384 |
| **Selected Experts per Token** | 8 |
| **Number of Shared Experts** | 1 |
| **Vocabulary Size** | $160 \times 10^3$ (160K) |
| **Context Length** | $128 \times 10^3$ (128K) tokens |
| **Attention Mechanism** | MLA |
| **Activation Function** | SwiGLU |
</div>

## 3. The Muon Breakthrough: Achieving Unprecedented Scale with Zero Instability

### The Muon Optimizer: Matrix-Aware Optimization

The [Muon optimizer](https://github.com/KellerJordan/Muon) represents a fundamental shift from traditional optimization approaches. Unlike AdamW or SGD that treat neural network parameters as vectors, **Muon exploits the matrix structure** of weight parameters, using geometry-aware updates and spectral norm constraints.

**Core Mathematical Innovation:**

$$W \leftarrow W - \eta \times \sqrt{\frac{\text{fan-out}}{\text{fan-in}}} \times \text{NewtonSchulz}(\nabla_W L)$$

Where $\text{NewtonSchulz}()$ performs orthogonalization using Newton-Schulz iteration:

$$\text{NewtonSchulz}(G) = \text{orthogonalize}(G) \text{ via iterative refinement}$$

$$X_{k+1} = aX_k + B_k X_k \text{ where } B_k = bA_k + cA_k^2, \; A_k = X_k X_k^T$$

This provides second-order-like benefits with minimal computational overhead (<1%).

### MuonClip: Scaling to Trillion Parameters

Kimi K2 represents the **first successful training of a trillion-parameter model** using the Muon optimizer family. Our **MuonClip** variant introduces critical innovations:

**Key Achievements:**
- **$10^{12}$ Parameter Scale**: Successfully trained the largest Muon-optimized model to date
- **$15.5 \times 10^{12}$ Token Training**: Completed full training with zero instability incidents  
- **$2\times$ Efficiency**: Achieved $\sim2\times$ computational efficiency compared to AdamW at scale
- **Perfect Stability**: Zero training instabilities throughout the entire process

### Technical Breakthroughs in MuonClip

1. **Extreme-Scale Stability**: Traditional optimizers face catastrophic failures beyond hundreds of billions of parameters. MuonClip's novel clipping and normalization techniques maintain stable gradients at trillion-parameter scales.

2. **MoE-Optimized Updates**: Specialized parameter update mechanisms for mixture-of-experts architectures, efficiently handling 32B activated parameters out of 1T total.

3. **Memory-Efficient Implementation**: Advanced techniques enabling trillion-parameter training on existing hardware infrastructure.

4. **Gradient Conditioning**: Matrix-aware orthogonalization provides superior gradient conditioning compared to vector-based optimizers.

### Why Muon Matters for AI

**Compared to AdamW:**
- 2× computational efficiency in large-scale training
- Better scaling properties without extensive hyperparameter tuning
- Superior convergence characteristics at extreme scales

**Matrix-Aware Advantages:**
- Direct exploitation of weight matrix structure
- Implicit regularization via spectral norm constraints  
- Improved gradient conditioning through orthogonalization
- Second-order benefits without Hessian computation overhead

### Research Foundation

This work builds on recent breakthroughs in optimizer research:
- **Original Muon**: Developed by Keller Jordan for geometry-aware optimization
- **Scaling Research**: Recent work showing Muon's superior scaling properties
- **Theoretical Foundation**: Matrix optimization theory applied to neural networks

> **Technical Details**: Full mathematical formulations and training procedures will be detailed in our upcoming research paper. MuonClip represents months of research into optimizer theory and distributed training at unprecedented scales.

## 4. Tool Calling Capabilities

### Native Tool Support

Kimi K2 has been specifically optimized for tool calling and agentic capabilities. The model:
- Does not have built-in native tools - all tools must be explicitly defined
- Accepts any custom tool definition following the OpenAI function schema
- Can chain multiple tools together autonomously
- Supports complex tool patterns including system commands, file operations, and API requests

### Creating Custom Tools

```python
# Example: Custom tool definition
tool = {
    "type": "function",
    "function": {
        "name": "execute_command",
        "description": "Execute a system command",
        "parameters": {
            "type": "object",
            "required": ["command"],
            "properties": {
                "command": {
                    "type": "string",
                    "description": "The command to execute"
                }
            }
        }
    }
}
```

### MCP (Model Context Protocol) Integration

**Yes, you can create an MCP bridge tool** that enables Kimi K2 to interface with any MCP server:

```python
mcp_bridge_tool = {
    "type": "function",
    "function": {
        "name": "mcp_server_request",
        "description": "Send requests to MCP servers",
        "parameters": {
            "type": "object",
            "required": ["server", "method", "params"],
            "properties": {
                "server": {
                    "type": "string",
                    "description": "MCP server identifier"
                },
                "method": {
                    "type": "string",
                    "description": "MCP method to call"
                },
                "params": {
                    "type": "object",
                    "description": "Method parameters"
                }
            }
        }
    }
}
```

This enables Kimi K2 to:
- Interface with filesystem, git, database, and other MCP servers
- Leverage the full MCP ecosystem
- Create autonomous agents with access to MCP tools

### Tool Exploration

Explore advanced tool capabilities with our comprehensive testing suite:

```bash
# Comprehensive tool capability exploration
python3 explore_tools.py

# Validate implementations against official guidance
python3 validate_tool_calling.py

# Quick functionality test
python3 quick_test.py
```

**`explore_tools.py`** demonstrates:
- Custom tool creation patterns for system commands, file operations, and API requests
- Tool chaining capabilities and multi-step workflows
- MCP (Model Context Protocol) integration possibilities
- Advanced agentic workflow patterns

**`validate_tool_calling.py`** provides:
- Compliance testing against official documentation
- Function signature compatibility validation
- Bug detection in implementation patterns
- Comprehensive error analysis and reporting

## 5. Deployment
> [!Note]
> You can access Kimi K2's API on https://platform.moonshot.ai , we provide OpenAI/Anthropic-compatible API for you.
>
> The Anthropic-compatible API maps temperature by `real_temperature = request_temperature * 0.6` for better compatible with existing applications.

Our model checkpoints are stored in the block-fp8 format, you can find it on [Huggingface](https://huggingface.co/moonshotai/Kimi-K2-Instruct).

Currently, Kimi-K2 is recommended to run on the following inference engines:

* vLLM
* SGLang
* KTransformers
* TensorRT-LLM

Deployment examples for vLLM and SGLang can be found in the [Model Deployment Guide](docs/deploy_guidance.md).

---

## 6. Model Usage

### Chat Completion

Once the local inference service is up, you can interact with it through the chat endpoint:

```python
def simple_chat(client: OpenAI, model_name: str):
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant created by Moonshot AI."},
        {"role": "user", "content": [{"type": "text", "text": "Please give a brief self-introduction."}]},
    ]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        stream=False,
        temperature=0.6,
        max_tokens=256
    )
    print(response.choices[0].message.content)
```

> [!NOTE]
> The recommended temperature for Kimi-K2-Instruct is `temperature = 0.6`.
> If no special instructions are required, the system prompt above is a good default.

---

### Tool Calling

Kimi-K2-Instruct has strong tool-calling capabilities.
To enable them, you need to pass the list of available tools in each request, then the model will autonomously decide when and how to invoke them.

The following example demonstrates calling a weather tool end-to-end:

```python
# Your tool implementation
def get_weather(city: str) -> dict:
    return {"weather": "Sunny"}

# Tool schema definition
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Retrieve current weather information. Call this when the user asks about the weather.",
        "parameters": {
            "type": "object",
            "required": ["city"],
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city"
                }
            }
        }
    }
}]

# Map tool names to their implementations
tool_map = {
    "get_weather": get_weather
}

def tool_call_with_client(client: OpenAI, model_name: str):
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant created by Moonshot AI."},
        {"role": "user", "content": "What's the weather like in Beijing today? Use the tool to check."}
    ]
    finish_reason = None
    while finish_reason is None or finish_reason == "tool_calls":
        completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.6,
            tools=tools,          # tool list defined above
            tool_choice="auto"
        )
        choice = completion.choices[0]
        finish_reason = choice.finish_reason
        if finish_reason == "tool_calls":
            messages.append(choice.message)
            for tool_call in choice.message.tool_calls:
                tool_call_name = tool_call.function.name
                tool_call_arguments = json.loads(tool_call.function.arguments)
                tool_function = tool_map[tool_call_name]
                tool_result = tool_function(**tool_call_arguments)
                print("tool_result:", tool_result)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call_name,
                    "content": json.dumps(tool_result)
                })
    print("-" * 100)
    print(choice.message.content)
```

The `tool_call_with_client` function implements the pipeline from user query to tool execution.
This pipeline requires the inference engine to support Kimi-K2’s native tool-parsing logic.
For streaming output and manual tool-parsing, see the [Tool Calling Guide](docs/tool_call_guidance.md).

