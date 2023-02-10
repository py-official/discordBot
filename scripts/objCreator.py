from jsonReader import getData
import disnake


def CreateEmbed(code):
    content = getData("contentData", "embed", code)
    embedTemp = disnake.Embed(
            title = content[0],
            description = content[1],
            color = 0xffffff
    )
    return embedTemp