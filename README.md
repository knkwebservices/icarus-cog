# icarus-cog

<img src="assets/banner.svg" alt="icarus-cog banner" width="100%">

A [Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot) cog for [Icarus](https://icarus.game/) players: look up items, weapons, recipes, creatures, talents, and more — pulled live from [Icarus Database](https://icarusdatabase.com).

## Features

- **`!icarus <name>`** — searches the Icarus Database and posts an embed for the best match: description, stats/properties, and a link to the full page
- Live lookups, not a bundled/stale dataset — every query hits icarusdatabase.com directly, respecting their crawl policy (1 request/second, cached for an hour)
- Falls back gracefully with a direct link if the full entry page can't be parsed

## Installation

This cog is installed the normal Red way, via the core Downloader cog:

```
[p]repo add icarus-cog https://github.com/knkwebservices/icarus-cog
[p]cog install icarus-cog icarus
[p]load icarus
```

(Replace `[p]` with your bot's command prefix.)

## Commands

| Command | Description |
|---|---|
| `!icarus <name>` | Look up an item, weapon, recipe, creature, talent, or more |
| `!ic <name>` | Alias for `!icarus` |

### Example

```
!icarus compound bow
```

## Credits

- Data courtesy of [Icarus Database](https://icarusdatabase.com), part of the [GDBN](https://gdbn.live/) network
- Built by [K & K Web Services](https://knkws.com)

## License

MIT
