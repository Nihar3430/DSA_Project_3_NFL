# Import And Initialize Pygame
import pygame
import sys
pygame.init()

# Get User Display Info
screenInfo = pygame.display.Info()
screenWidth = screenInfo.current_w  # Full screen width
screenHeight = screenInfo.current_h  # Full screen height

# Set Program Window Dimensions
windowWidth = int(screenWidth * 0.8)  # 80% of the screen width
windowHeight = int(screenHeight * 0.8)  # 80% of the screen height

# Create Bordered Window
screen = pygame.display.set_mode((windowWidth, windowHeight), pygame.RESIZABLE)
pygame.display.set_caption("Team Comparison")

# Color Values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 40)  # Default font, size 40

# Logo
# Black Placeholder
teamLogo = pygame.Surface((100, 100))
teamLogo.fill(BLACK)

# Team Data
team1Data = {
    "name": "Team 1",
    "stats": ["Average Points Scored: 30", "Average Total Yards: 400",
              "Average Yards Per Carry: 4.2", "Average Passing Yards: 250",
              "Average Rushing Yards: 150"]
}

team2Data = {
    "name": "Team 2",
    "stats": ["Average Points Scored: 28", "Average Total Yards: 380",
              "Average Yards Per Carry: 3.8", "Average Passing Yards: 240",
              "Average Rushing Yards: 140"]
}

favoredTeam = "Favored To Win: Team Name"
winPercent = "Win %: 60%"

# Function To Write Text
def writeText(text, xCoor, xCoor, color=BLACK):
    textSurface = font.render(text, True, color)
    screen.blit(textSurface, (xCoor, xCoor))

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # White Background Placeholder
    screen.fill(WHITE)

    # Draw Team Left Side
    screen.blit(teamLogo, (50, 50))
    writeText(team1Data["name"], 50, 160)
    for i, stat in enumerate(team1Data["stats"]):
        writeText(stat, 50, 200 + i * 30)

    # Draw VS
    writeText("V.S.", windowWidth // 2 - 50, windowHeight // 2 - 20, BLACK)

    # Draw Team 2 Right Side
    screen.blit(teamLogo, (windowWidth - 150, 50))
    writeText(team2Data["name"], windowWidth - 150, 160)
    for i, stat in enumerate(team2Data["stats"]):
        writeText(stat, windowWidth - 350, 200 + i * 30)

    # Draw Favored Team Section
    writeText(favoredTeam, windowWidth // 2 - 150, 20)
    writeText(winPercent, windowWidth // 2 - 50, 60)

    # Refresh Display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
