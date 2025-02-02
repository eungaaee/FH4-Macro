# Forza Horizon 4 Skill Point and Wheelspin Macro

## Introduction
This project provides a macro to automate the process of earning skill points and wheelspins in Forza Horizon 4.

## Features
- Automates skill point farming (using Super7 challenge card)
- Automates wheelspin farming (Toyota Supra RZ Perk)

## How to use
### Skill Point
> Watch the skill point farming guide here. [@jeremiepogi](https://www.youtube.com/watch?v=gOFWmkAjO9U)  
> Tested with a Renault 5 Turbo FE.
1. Place your ramp in the Super7 challenge card.
2. Do "Barrel Roll" Once.
3. While the car is stop in the air performing a "Barrel Roll", start the script.
4. The macro will automatically start farming.
### Wheelspin
1. In the "Autoshow" menu, start the macro script.
2. The macro will automatically repeat buying a Toyota Supra RZ and unlocking perks.
### Discord Notify Bot
1. Make your empty bot in [here](https://discord.com/developers).
2. Make the new server and invite the bot.
3. Add your token in `/src/config.py`

    ```python
    # /src/config.py
    DISCORD_BOT_TOKEN = "your_token"
    ```
4. Run any macro script.

## References
### Discord Notify Bot
- [Discord.py Github Repository](https://py.delta.chat)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/index.html)

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, please open an issue on GitHub.