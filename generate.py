import os

# GitHub Pages base URL
base_url = "https://touchmetender.github.io/GameFiles/games"

# Game folder location after cloning
games_directory = "GameFiles/games"
output_path = "generated/games.html"

# Make sure output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# List and sort games
game_dirs = sorted(
    [d for d in os.listdir(games_directory) if os.path.isdir(os.path.join(games_directory, d))]
)

# Write HTML
with open(output_path, "w", encoding="utf-8") as f:
    for game in game_dirs:
        game_url = f"{base_url}/{game}/index.html"
        thumbnail_url = f"{base_url}/{game}/thumbnail.jpg"
        game_name = game.replace('-', ' ').title()
        f.write(f'''
<div class="grid-item" onclick="openGame('{game_url}')">
  <img src="{thumbnail_url}" alt="{game_name}" />
  <div class="name">{game_name}</div>
</div>
''')

print("✅ Game blocks saved to generated/games.html")
