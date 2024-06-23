from anthropic import AnthropicBedrock

client = AnthropicBedrock(

    aws_region="us-west-2",
)

message = client.messages.create(
    model="anthropic.claude-3-sonnet-20240229-v1:0",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}]
)
print(message.content)