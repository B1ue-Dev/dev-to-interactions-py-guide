import interactions

client = interactions.Client(token="your_bot_token_here")

@client.command(
    name="ping",
    description="Ping pong",
    scope=your_guild_id_here
)
async def _ping(ctx: interactions.CommandContext):
    await ctx.send("Pong!")

@client.event
async def on_ready():
    print("Ready!")

client.start()