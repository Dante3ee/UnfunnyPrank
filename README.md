# UnfunnyPrank
*UnfunnyPrank* is a small Python script that mutes all active applications on your Windows system.
It also generates a script called remedy.py that restores the sound and clean up auxiliary files like README and LICENSE.

Its just made to annoy your friend with a fast 

```bash 
git clone https://github.com/Dante3ee/UnfunnyPrank.git

python unfunny_prank.py
```
And to clean, simply run 
```bash
python remedy.py
```
 ## How it Works

The main script toggles the system audio state using the pycaw library.
It checks if pycaw is already installed; if not, it installs it and removes it after execution.
remedy.py restores audio and delete README and LICENSE files.
```mermaid
flowchart TD
    %% unfunny_prank.py
    A1[Start UnfunnyPrank] --> B1{Is pycaw installed}
    B1 -- No --> C1[Install pycaw]
    B1 -- Yes --> D1[Skip installation]

    C1 --> E1[Toggle sound]
    D1 --> E1[Toggle sound]
    E1 --> F1[Create remedy script]

    F1 --> G1{PyCaw installed by script}
    G1 -- Yes --> H1[Append uninstall pycaw to remedy]
    G1 -- No --> I1[Do nothing]

    H1 --> J1[Write remedy.py and self-delete]
    I1 --> J1
    J1 --> K1[Delete UnfunnyPrank script]
    K1 --> L1[End UnfunnyPrank]

    %% remedy.py
    A2[Start remedy script]
    A2 --> B2[Restore sound]
    B2 --> C2[Delete README and LICENSE]
    C2 --> D2{PyCaw uninstall included}
    D2 -- Yes --> E2[Uninstall pycaw]
    D2 -- No --> F2[Do nothing]
    E2 --> G2[Delete remedy.py]
    F2 --> G2
    G2 --> H2[End remedy script]
