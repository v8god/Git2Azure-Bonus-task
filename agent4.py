from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

class ASI1miniRequest(Model):
    query: str

class ASI1miniResponse(Model):
    response: str

agent = Agent(
        name = "Agent 2009",
        seed = "4thAgent",
        port = 2009,
        endpoint = ["http://localhost:2009/submit"],
        mailbox = True
)
fund_agent_if_low;{agent.wallet.address()}

agent_address = agent.address

@agent.on_event("startup")
#@agent.on_interval(period=5)
async def startup(ctx:Context):
    ctx.logger.info(f"Hello Boss!, I am {agent.name}")
    ctx.logger.info(f"Hello, My Address is {agent.address}")
    query = input("Enter Your Query...= ")
    await ctx.send(agent_address,ASI1miniResponse(query = query))

@agent.on_message(model= ASI1miniResponse)
async def receiver(ctx:Context, sender:str, msg:ASI1miniResponse):
    ctx.logger.info(msg.response)


@agent.on_event("shutdown")
async def shutdown(ctx:Context):
    ctx.logger.info(f"Bye Boss! Until Next time.")
    ctx.logger.info(f"  ______                  ________")
    ctx.logger.info(f"||      \    \\\    //   ||")
    ctx.logger.info(f"||      /     \\\  //    ||")
    ctx.logger.info(f"||======       \\\//     ||_____")
    ctx.logger.info(f"||      \       ||      ||")
    ctx.logger.info(f"||       |      ||      ||")
    ctx.logger.info(f"||______/       ||      ||________")


if __name__ == "__main__":
    agent.run()
