import disnake




embed = {"ErrorNo" : ["Successful!!", "Starting server"],
	"ErrorServerHasAlreadyStarted" :["Error x 1", "Server has already started"],
	"ErrorNoStop" : ["Successful!!", "Stopping server"]
	}

def CreateEmbed(code):
    content = embed[code]
    embedTemp = disnake.Embed(
            title = content[0],
            description = content[1],
            color = 0xffffff
    )
    return embedTemp
