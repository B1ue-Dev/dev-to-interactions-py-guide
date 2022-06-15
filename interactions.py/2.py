import interactions

client = interactions.Client(token="your_bot_token_here")

button =[
    interactions.ActionRow(
        components=[
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                label="Click me!",
                custom_id="click_me",
            ),
            interactions.Button(
                style=interactions.ButtonStyle.DANGER,
                label="Do not click!",
                custom_id="do_not_click",
            ),
        ]
    )
]

@client.command(
    name="button",
    description="Send a button",
)
async def _button(ctx: interactions.CommandContext):
    await ctx.send(components=button)

@client.component("click_me")
async def click_me(ctx: interactions.ComponentContext):
    await ctx.send("Clicked!")

@client.component("do_not_click")
async def do_not_click(ctx: interactions.ComponentContext):
    await ctx.send("You clicked the wrong button!")

@client.event
async def on_ready():
    print("Ready!")

client.start()