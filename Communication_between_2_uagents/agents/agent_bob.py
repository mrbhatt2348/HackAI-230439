from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
 
class Message(Model): 
    message: str
 
bob = Agent(
    name="bob",
    port=8001,
    seed="bob secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)
 
fund_agent_if_low(bob.wallet.address())
 
@bob.on_message(model=Message)
async def message_handler(ctx: Context, msg: Message):
    ctx.logger.info(f"Received message: {msg.message}")
 
if __name__ == "__main__":
    bob.run()
