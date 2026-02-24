# Car Detailer Marketing Agent - Setup Guide

## Prerequisites

- Python 3.9 or higher
- Anthropic API key (free tier available)
- Git

## Step 1: Clone or Download

```bash
git clone https://github.com/skyduggan/car-detailer-marketing-agent.git
cd car-detailer-marketing-agent
```

## Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Set Up API Key

### Option A: Environment Variable

```bash
# Windows
set ANTHROPIC_API_KEY=sk-your-key-here

# macOS/Linux
export ANTHROPIC_API_KEY=sk-your-key-here
```

### Option B: Create .env File

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=sk-your-key-here
```

Then update `main.py` to load it:

```python
from dotenv import load_dotenv
load_dotenv()
```

## Step 5: Get Your API Key

1. Visit [Anthropic Console](https://console.anthropic.com)
2. Sign up or log in
3. Navigate to API keys
4. Create a new API key
5. Copy the key and add to your environment

## Step 6: Customize for Your Business

Edit the `DetailingClient` in `main.py`:

```python
client = DetailingClient(
    name="Your Business Name",
    email="your@email.com",
    phone="555-1234",
    business_type="independent",  # or "franchise", "dealership"
    service_area="Your City, State",
    monthly_budget=2000,  # Your marketing budget
    goals=["Increase leads", "Build brand awareness"]
)
```

## Step 7: Run the Agent

```bash
python main.py
```

## Step 8: Advanced Features (Optional)

For advanced features, run:

```bash
python advanced_agent.py
```

## Quick Examples

### Example 1: Generate Strategy Only

```python
from main import CarDetailerMarketingAgent, DetailingClient

agent = CarDetailerMarketingAgent()
client = DetailingClient(
    name="Auto Shine",
    email="info@autoshine.com",
    phone="555-5555",
    business_type="independent",
    service_area="Denver, CO",
    monthly_budget=1500,
    goals=["Grow leads", "Increase revenue"]
)

strategy = agent.generate_marketing_strategy(client)
print(strategy)
```

### Example 2: Generate Social Content

```python
from main import CarDetailerMarketingAgent

agent = CarDetailerMarketingAgent()
content = agent.create_social_media_content("Paint Protection Film", num_posts=5)
print(content)
```

### Example 3: Email Campaign

```python
agent = CarDetailerMarketingAgent()
emails = agent.generate_email_campaign("New Customers", "Welcome Series")
print(emails)
```

### Example 4: Pricing Strategy

```python
agent = CarDetailerMarketingAgent()
pricing = agent.generate_pricing_strategy("small", "premium", "Miami, FL")
print(pricing)
```

## Troubleshooting

### "API Key not found"
- Check that your API key is set correctly
- Restart your terminal/IDE after setting environment variables
- Verify the key format starts with `sk-`

### "Module not found"
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again
- Check Python version is 3.9+

### "Rate limit exceeded"
- Wait a few moments before making another request
- Check your Anthropic account for usage limits
- Consider upgrading your plan if needed

### "Incomplete response"
- Try again - sometimes the API times out
- Reduce `max_tokens` in the code if needed
- Check your internet connection

## Customization Tips

### Change Model
```python
self.model = "claude-3-opus-20240229"  # Use different Claude version
```

### Adjust Token Limits
```python
response = self.client.messages.create(
    model=self.model,
    max_tokens=3000,  # Increase for longer responses
    ...
)
```

### Add Custom Industry Knowledge
```python
def _load_marketing_knowledge(self) -> str:
    return """
    Your custom knowledge base here
    """
```

### Save Outputs to File

```python
with open("strategy_output.txt", "w") as f:
    f.write(strategy)
```

## Next Steps

1. **Run the basic agent** and review the output
2. **Customize the client profile** for your business
3. **Generate strategies** for your specific needs
4. **Implement recommendations** into your marketing plan
5. **Try advanced features** for deeper analysis
6. **Iterate and refine** based on results

## Support & Resources

- [Anthropic Documentation](https://docs.anthropic.com)
- [Claude API Guide](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [Car Detailing Marketing Blog](https://example.com)

## License

MIT - Use freely with attribution

---

Questions? Open an issue on the GitHub repository!
