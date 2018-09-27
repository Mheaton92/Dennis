NAME = "list items"
USAGE = "list items"
DESCRIPTION = "(WIZARDS ONLY) List all items in the world."


def COMMAND(console, database, args):
    if len(args) != 0:
        console.msg("Usage: " + USAGE)
        return False

    # Make sure we are logged in, and a wizard.
    if not console.user:
        console.msg(NAME + ": must be logged in first")
        return False
    if not console.user["wizard"]:
        console.msg(NAME + ": you do not have permission to use this command")
        return False

    items = database.items.find().sort("id", 1)
    if items.count():
        for i in items:
            console.msg(str(i["id"]) + ": " + i["name"])
    else:
        console.msg(NAME + ": no items")

    return True
